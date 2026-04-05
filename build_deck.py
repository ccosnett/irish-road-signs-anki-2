#!/usr/bin/env python3
"""Build an Anki deck from Irish road sign images.

Each image becomes a flashcard:
  - Front: the road sign image
  - Back: the description (extracted from the filename)
"""

import glob
import os
import hashlib
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
    css=".card { text-align: center; font-size: 24px; } img { max-width: 400px; max-height: 400px; }",
)

deck = genanki.Deck(DECK_ID, "Irish Road Signs")
media_files = []

image_files = sorted(glob.glob("*.png"))

for image_path in image_files:
    filename = os.path.basename(image_path)
    name_without_ext = os.path.splitext(filename)[0]
    description = name_without_ext.replace("_", " ")

    # Generate a stable GUID from the filename
    guid_hash = hashlib.md5(filename.encode()).hexdigest()[:10]

    note = genanki.Note(
        model=model,
        fields=[
            f'<img src="{filename}">',
            description,
        ],
        guid=guid_hash,
    )
    deck.add_note(note)
    media_files.append(image_path)

package = genanki.Package(deck)
package.media_files = media_files
package.write_to_file("irish_road_signs.apkg")

print(f"Created irish_road_signs.apkg with {len(media_files)} cards")
