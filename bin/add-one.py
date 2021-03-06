#!/usr/bin/env python3

from datetime import datetime
from pathlib import Path
import getopt
import os
import sys

HELP = "add-one.py -t <term> -d <definition> [-l <link>] [-s <slug>]"


def file_content(term, definition, link=None, slug=None):
    today = datetime.today().strftime('%Y-%m-%d')

    txt = "+++\n"
    txt += "title = \"%s\"\n" % term
    txt += "date = %s\n" % today
    if slug:
        txt += "slug = \"%s\"\n" % slug
    if link:
        txt += "[extra]\n"
        txt += "link = \"%s\"\n" % link
    txt += "+++\n"
    txt += "%s\n\n" % definition

    return txt


def new_term(term, definition, link=None, slug=None):
    this_file = Path(os.path.realpath(__file__))
    content_dir = os.path.join(this_file.parent.parent, "content")

    filename = term.lower()
    if slug:
        filename = slug.lower()
    filename = filename + ".md"

    md_file = os.path.join(content_dir, filename)
    if os.path.exists(md_file):
        raise Exception("file already exists: %s" % filename)

    content = file_content(term, definition, link, slug)
    with open(md_file, 'w') as f:
        f.write(content)

    print("Created %s" % md_file)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ht:d:l:s:", ["term=", "definition=", "link=", "slug="])
    except getopt.GetoptError:
        print(HELP)
        sys.exit(2)

    term, definition, link, slug = None, None, None, None

    for opt, arg in opts:
        if opt == '-h':
            print(HELP)
            sys.exit()
        elif opt in ("-t", "--term"):
            term = arg
        elif opt in ("-d", "--definition"):
            definition = arg
        elif opt in ("-l", "--link"):
            link = arg
        elif opt in ("-s", "--slug"):
            slug = arg

    if not term or not definition:
        print("Term and definition are required. See -h")
        sys.exit(1)

    try:
        new_term(term, definition, link, slug)
    except Exception as e:
        print("ERROR: %s" % e)


if __name__ == "__main__":
    main(sys.argv[1:])
