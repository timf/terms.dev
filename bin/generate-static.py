#!/usr/bin/env python3

from pathlib import Path
import glob
import json
import os
import re

this_file = Path(os.path.realpath(__file__))
content_dir = os.path.join(this_file.parent.parent, "content")
os.chdir(content_dir)


def parse_one(file_path):
    """This is not particularly robust but will do it"""
    term = None
    definition = None
    link = None
    marker1 = False
    marker2 = False
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == "":
                continue
            elif marker1 and marker2:
                definition = line.strip()
                break
            elif line.strip() == "+++":
                if not marker1:
                    marker1 = True
                elif not marker2:
                    marker2 = True
                else:
                    raise Exception("expected only two +++")
            elif line[:5] == "title":
                if marker1 and not marker2:
                    m = re.search('title = "(.+)"', line)
                    term = m.group(1)
                    if not term:
                        raise Exception("parser confused with title =")
            elif line[:4] == "link":
                if marker1 and not marker2:
                    m = re.search('link = "(.+)"', line)
                    link = m.group(1)
                    if not link:
                        raise Exception("parser confused with link =")

    if not term:
        raise Exception("could not parse term (title) from %s" % file_path)
    if not definition:
        raise Exception("could not parse definition from %s" % file_path)

    return term, definition, link


to_json = []
to_write = []
for file in glob.glob("*.md"):
    if file == "_index.md":
        continue
    term, definition, link = parse_one(file)
    to_write.append("%s: %s\n" % (term, definition))
    to_json.append({'term': term, 'definition': definition, 'link': link})


static_dir = os.path.join(this_file.parent.parent, "static")
txt_file_path = os.path.join(static_dir, "terms.txt")
json_file_path = os.path.join(static_dir, "terms.json")
json_txt = json.dumps(to_json, indent=4, sort_keys=True)

with open(txt_file_path, 'r') as f:
    current_content = f.readlines()

if current_content == to_write:
    print("No change.")
else:
    with open(txt_file_path, 'w') as f:
        for line in to_write:
            f.write(line)
    print("Wrote file: %s" % txt_file_path)
    with open(json_file_path, 'w') as f:
        f.write(json_txt)
    print("Wrote file: %s" % json_file_path)