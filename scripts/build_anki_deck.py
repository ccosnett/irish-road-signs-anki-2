#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import itertools
import json
import re
import sqlite3
import tempfile
import zipfile
from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "irish-road-signs.apkg"
DECK_NAME = "Irish Road Signs"
DECK_ID = 2054517318
MODEL_ID = 1677345012
BUILD_TIMESTAMP = 1.0
ZIP_DATE_TIME = (2024, 1, 1, 0, 0, 0)


def humanize_stem(stem: str) -> str:
    text = stem.replace("_", " ")
    text = re.sub(r"\bkm per hour\b", "km/h", text)
    text = re.sub(r"\bhgv\b", "HGV", text, flags=re.IGNORECASE)
    text = re.sub(r"\bu turn\b", "U-turn", text, flags=re.IGNORECASE)
    text = re.sub(r"\bcul de sac\b", "Cul-de-sac", text, flags=re.IGNORECASE)
    text = re.sub(r"\bm\b(?=\d)", "M", text)
    return text[:1].upper() + text[1:]


def guid_for_name(name: str) -> str:
    digest = hashlib.sha1(name.encode("utf-8")).hexdigest()
    return digest[:10]


def build_deck() -> tuple[genanki.Deck, list[str]]:
    model = genanki.Model(
        MODEL_ID,
        "Irish Road Sign Basic",
        fields=[
            {"name": "Image"},
            {"name": "Description"},
        ],
        templates=[
            {
                "name": "Sign -> Description",
                "qfmt": '<div class="prompt">{{Image}}</div>',
                "afmt": (
                    '{{FrontSide}}<hr id="answer">'
                    '<div class="answer">{{Description}}</div>'
                ),
            }
        ],
        css="""
        .card {
          font-family: Arial, sans-serif;
          font-size: 26px;
          text-align: center;
          color: #111;
          background-color: #fff;
          padding: 24px 16px;
        }
        .prompt img {
          max-width: 95%;
          max-height: 70vh;
          object-fit: contain;
        }
        .answer {
          font-size: 30px;
          line-height: 1.35;
          font-weight: 600;
        }
        #answer {
          margin: 24px auto;
          max-width: 320px;
        }
        """,
    )

    deck = genanki.Deck(DECK_ID, DECK_NAME)
    media_files: list[str] = []

    for image_path in sorted(ROOT.glob("*.png")):
        description = humanize_stem(image_path.stem)
        note = genanki.Note(
            model=model,
            fields=[
                f'<img src="{image_path.name}">',
                description,
            ],
            guid=guid_for_name(image_path.name),
        )
        deck.add_note(note)
        media_files.append(str(image_path))

    return deck, media_files


def write_deterministic_package(
    deck: genanki.Deck, media_files: list[str], output_file: Path
) -> None:
    package = genanki.Package(deck, media_files=media_files)
    db_fd, db_filename = tempfile.mkstemp()

    try:
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()
        id_gen = itertools.count(int(BUILD_TIMESTAMP * 1000))
        package.write_to_db(cursor, BUILD_TIMESTAMP, id_gen)
        conn.commit()
        conn.close()

        media_json = {
            idx: Path(path).name for idx, path in enumerate(media_files)
        }

        with zipfile.ZipFile(output_file, "w") as outzip:
            collection_info = zipfile.ZipInfo("collection.anki2", date_time=ZIP_DATE_TIME)
            collection_info.compress_type = zipfile.ZIP_STORED
            with open(db_filename, "rb") as handle:
                outzip.writestr(collection_info, handle.read())

            media_info = zipfile.ZipInfo("media", date_time=ZIP_DATE_TIME)
            media_info.compress_type = zipfile.ZIP_STORED
            outzip.writestr(
                media_info,
                json.dumps(media_json, sort_keys=True, separators=(",", ":")).encode("utf-8"),
            )

            for idx, path in enumerate(media_files):
                media_path = Path(path)
                file_info = zipfile.ZipInfo(str(idx), date_time=ZIP_DATE_TIME)
                file_info.compress_type = zipfile.ZIP_STORED
                outzip.writestr(file_info, media_path.read_bytes())
    finally:
        Path(db_filename).unlink(missing_ok=True)


def main() -> None:
    deck, media_files = build_deck()
    OUTPUT_DIR.mkdir(exist_ok=True)
    write_deterministic_package(deck, media_files, OUTPUT_FILE)
    print(f"Wrote {OUTPUT_FILE}")
    print(f"Cards: {len(media_files)}")


if __name__ == "__main__":
    main()
