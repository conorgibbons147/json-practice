#!/bin/python3

import json

with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('../../data/chacon.csv', 'a') as file:
    for repo in data[:5]:
        name = repo.get('name')
        html_url = repo.get('html_url')
        updated_at = repo.get('updated_at')
        visibility = repo.get('visibility')
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        file.write(line)

print("chacon.csv has been updated")
