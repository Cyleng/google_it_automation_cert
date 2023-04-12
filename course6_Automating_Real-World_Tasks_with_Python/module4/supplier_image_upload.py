#! /usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"

image_folder = "supplier-data/images/"

for image in os.listdir(image_folder):
    if (not image.startswith('.')) and image.endswith('jpeg'):
        with open(image_folder + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
