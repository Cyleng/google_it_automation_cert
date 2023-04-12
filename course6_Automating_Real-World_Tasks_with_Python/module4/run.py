#! /usr/bin/env python3

import os
import requests

url = "http://34.173.153.71/fruits/"

description_folder = "supplier-data/descriptions/"

for description in os.listdir(description_folder):
    if (not description.startswith('.')) and description.endswith('txt'):
        with open(description_folder + description, 'r') as opened:
            lines = opened.readlines()
            name = lines[0].strip()
            weight = int(lines[1].strip().strip('lbs'))
            description_content = lines[2].strip()
            #remove .txt from the end of the file name
            image_name = description[:-4] + '.jpeg'
            data = {'name': name, 'weight': weight,
                    'description': description_content, 'image_name': image_name}
            #print(data)
            r = requests.post(url, json=data)
            r.raise_for_status()
