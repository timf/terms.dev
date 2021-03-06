#!/usr/bin/env python3

from _ import tdlib
import getopt
import sys

HELP = "add-one.py -t <term> -d <definition> [-l <link>] [-s <slug>]"


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
        tdlib.new_term(term, definition, link=link, slug=slug)
    except Exception as e:
        print("ERROR: %s" % e)


if __name__ == "__main__":
    main(sys.argv[1:])
