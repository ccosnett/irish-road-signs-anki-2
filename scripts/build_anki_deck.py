#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import re
from pathlib import Path

import genanki


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "dist"
OUTPUT_FILE = OUTPUT_DIR / "irish-road-signs.apkg"
DECK_NAME = "Irish Road Signs"
DECK_ID = 2054517318
MODEL_ID = 1677345012


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


def main() -> None:
    deck, media_files = build_deck()
    OUTPUT_DIR.mkdir(exist_ok=True)
    genanki.Package(deck, media_files=media_files).write_to_file(str(OUTPUT_FILE))
    print(f"Wrote {OUTPUT_FILE}")
    print(f"Cards: {len(media_files)}")


if __name__ == "__main__":
    main()
