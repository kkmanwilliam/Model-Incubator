'''
this script would make directory be flat
before:
    - folder
        - sub-folder1
            - 1.jpg
            - 2.jpg
        - sub-folder2
            - 3.jpg
after:
    - folder-preprocess
        - 1.jpg
        - 2.jpg
        - 3.jpg
'''
import argparse
from pathlib import Path

import tqdm

import cv2

PARSER = argparse.ArgumentParser(
    description='Search picture with the most similar angle')
PARSER.add_argument('-i', '--inputdir', dest='imgfolder', required=True, help='the directory contains images')
ARGS = PARSER.parse_args()

IMGFOLER_NAME = ARGS.imgfolder
for i in Path(ARGS.imgfolder).suffixes:
    IMGFOLER_NAME = IMGFOLER_NAME.replace(i, '')
ROOT = Path(IMGFOLER_NAME).parent.resolve()
for directory in Path(IMGFOLER_NAME).iterdir():
    if directory.is_dir():
        PREPROC_FOLDER = ROOT / (str(directory.name) + '_preprocess')
        print(PREPROC_FOLDER)
        PREPROC_FOLDER.mkdir(exist_ok=True)
        for index, filepath in tqdm.tqdm(enumerate(directory.glob('**/*.*'))):
            try:
                cv2.imread(str(filepath)).shape
            except Exception:
                # print("not image")
                continue
            suffix = filepath.suffix
            if suffix.lower() == '.jpg' or suffix.lower() == '.jpeg':
                suffix = '.jpg'
            elif suffix.lower() == '.png':
                suffix = '.png'
            filepath.rename(PREPROC_FOLDER / (str(index)+suffix))
