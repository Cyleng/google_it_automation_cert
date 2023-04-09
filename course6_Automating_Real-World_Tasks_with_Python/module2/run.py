#! /usr/bin/env python3

import os
import requests

feedbacks_folder = "./data/feedback/"

target_url = ""

if __name__ == "__main__":
    for file in os.listdir(feedbacks_folder):
        with open(feedbacks_folder + file) as f:
            feedback = {}
            feedback["title"] = f.readline().strip()
            feedback["name"] = f.readline().strip()
            feedback["date"] = f.readline().strip()
            feedback["feedback"] = f.read().strip()
            response = requests.post(target_url, json=feedback)
            print(response.status_code)
