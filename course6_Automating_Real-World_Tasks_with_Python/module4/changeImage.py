#! /usr/bin/env python3

import os

from PIL import Image


for file in os.listdir('supplier-data/images'):
  if file.endswith('.tiff'):
    im = Image.open('supplier-data/images/' + file)
    im.convert('RGB').resize((600, 400)).save('supplier-data/images/' + file[:-5] + '.jpeg', 'JPEG')



