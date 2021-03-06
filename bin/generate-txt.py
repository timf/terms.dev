#!/usr/bin/env python3

from pathlib import Path
import glob
import os
import re

this_file = Path(os.path.realpath(__file__))
content_dir = os.path.join(this_file.parent.parent, "content")
os.chdir(content_dir)


def parse_one(file_path):
    """This is not particularly robust but will do it"""
    term = None
    definition = None
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

    if not term:
        raise Exception("could not parse term (title) from %s" % file_path)
    if not definition:
        raise Exception("could not parse definition from %s" % file_path)

    return term, definition


to_write = []
for file in glob.glob("*.md"):
    if file == "_index.md":
        continue
    term, definition = parse_one(file)
    to_write.append("%s: %s" % (term, definition))


static_dir = os.path.join(this_file.parent.parent, "static")
txt_file_path = os.path.join(static_dir, "terms.txt")

with open(txt_file_path, 'w') as f:
    for line in to_write:
        f.write(line)
        f.write("\n")

print("Wrote file: %s" % txt_file_path)
