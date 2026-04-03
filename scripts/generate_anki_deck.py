#!/usr/bin/env python3
"""Generate an Anki deck from Irish road sign images.

Each image becomes a flashcard where:
- Front (question): the road sign image
- Back (answer): the description extracted from the filename
"""

import glob
import hashlib
import os
import sys

import genanki

DECK_ID = 2059400110
MODEL_ID = 1607392319

model = genanki.Model(
    MODEL_ID,
    "Irish Road Signs",
    fields=[
        {"name": "Image"},
        {"name": "Description"},
    ],
    templates=[
        {
            "name": "Sign → Description",
            "qfmt": "{{Image}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Description}}',
        },
    ],
)


def description_from_filename(filename: str) -> str:
    """Convert a filename like 'no_right_turn.png' to 'No Right Turn'."""
    name = os.path.splitext(filename)[0]
    return name.replace("_", " ").title()


def stable_guid(filename: str) -> str:
    """Generate a stable GUID from the filename so cards persist across rebuilds."""
    return hashlib.sha256(filename.encode()).hexdigest()[:10]


def build_deck(image_dir: str, output_path: str) -> None:
    deck = genanki.Deck(DECK_ID, "Irish Road Signs")
    package = genanki.Package(deck)
    media_files = []

    image_extensions = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
    image_files = sorted(
        f
        for f in os.listdir(image_dir)
        if os.path.splitext(f)[1].lower() in image_extensions
    )

    if not image_files:
        print("No image files found.", file=sys.stderr)
        sys.exit(1)

    for filename in image_files:
        filepath = os.path.join(image_dir, filename)
        description = description_from_filename(filename)
        note = genanki.Note(
            model=model,
            fields=[f'<img src="{filename}">', description],
            guid=stable_guid(filename),
        )
        deck.add_note(note)
        media_files.append(filepath)

    package.media_files = media_files
    package.write_to_file(output_path)
    print(f"Generated {output_path} with {len(image_files)} cards.")


if __name__ == "__main__":
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output = os.path.join(repo_root, "irish_road_signs.apkg")
    build_deck(repo_root, output)
