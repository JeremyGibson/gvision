#!/usr/bin/python
import os
from pathlib import Path
from datetime import datetime
from google.cloud import vision

LOG_PATH = Path("logs")
PATH_TO_IMAGES = Path(os.environ["PHOTOS_DIR"])

client = vision.ImageAnnotatorClient()

POTENTIAL_DOCUMENT = ['font', 'material property', 'parallel', 'stationery', 'recipe', 'paper', 'paper product',
                      'letter', 'document', 'post-it note', 'screenshot', '']


def is_paper(labels: list):
    test = [x for x in labels if x in POTENTIAL_DOCUMENT]
    match_per = len(test) / len(POTENTIAL_DOCUMENT)
    if len(test) > 0:
        return True, match_per
    return False, match_per


def get_file():
    images = [".jpg", ".png"]
    for p in PATH_TO_IMAGES.glob("**/*.*"):
        if p.suffix.lower() in images:
            yield p


def label_maker():
    log = LOG_PATH / f"potential_documents_{datetime.now()}.log"
    with log.open('w') as logfh:
        for f in get_file():
            print(f"Examining: {f}")
            with f.open('rb') as fh:
                content = fh.read()
            image = vision.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations
            labels = [x.description.lower() for x in labels]
            potential, percentage = is_paper(labels)
            if potential:
                print(f"{f} is probably a document.")
                logfh.write(f"{f}: {percentage}  {labels}\n")


if __name__ == "__main__":
    label_maker()
