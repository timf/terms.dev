#!/usr/bin/env python3

from _ import tdlib
import csv
import getopt
import json
import sys

HELP = """add-many.py -c <csv file> [ -d / --dryrun]
add-many.py -j <json file> [ -d / --dryrun]

For CSV, this order is expected: <term>,<definition>,<slug>,<link>
  -> slug and link are optional. If missing, the 3rd and 4th CSV fields still needs to be present.

For JSON, an array of objects is expected, each with fields: term, definition, slug, link
  -> slug and link fields are optional. If they are empty strings, it is like they are missing.
"""


def read_csv(csv_path, dryrun=False):
    with open(csv_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',', dialect='excel')
        count = 0
        for row in reader:
            count += 1
            if len(row) == 0:
                # blank line, skip it
                continue
            if len(row) != 4:
                raise Exception("expects four CSV fields in each row. In file '%s' there are %d "
                                "fields on line %d" % (csv_path, len(row), count))
            term = row[0].strip()
            definition = row[1].strip()
            slug = row[2].strip()
            link = row[3].strip()
            tdlib.new_term(term, definition, link=link, slug=slug, dryrun=dryrun)


def json_field_missing(field, item, file_path):
    return "an item in the JSON file '%s' is missing the '%s' field. " \
           "Rest of the item: %s" % (file_path, field, item)


def read_json(json_path, dryrun=False):
    """Sample JSON:

    [
        {
            "term": "blah" ,
            "definition": "some definition 1" ,
            "link": "https://..." ,
            "slug": "blah1"
        },
        {
            "term": "blah2" ,
            "definition": "some definition 2" ,
            "link": "https://..." ,
            "slug": "blah2"
        }
    ]
    """
    with open(json_path) as json_file:
        data = json.load(json_file)
        for item in data:
            if "term" in item:
                term = item["term"].strip()
            else:
                raise Exception(json_field_missing("term", item, json_path))
            if "definition" in item:
                definition = item["definition"].strip()
            else:
                raise Exception(json_field_missing("definition", item, json_path))
            link = None
            if "link" in item:
                link = item["link"].strip()
            slug = None
            if "slug" in item:
                slug = item["slug"].strip()
            tdlib.new_term(term, definition, link=link, slug=slug, dryrun=dryrun)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hdc:j:", ["csv=", "json=", "dryrun"])
    except getopt.GetoptError:
        print(HELP)
        sys.exit(2)

    csv_path, json_path = None, None
    dryrun = False

    for opt, arg in opts:
        if opt == '-h':
            print(HELP)
            sys.exit()
        elif opt in ("-c", "--csv"):
            csv_path = arg
        elif opt in ("-d", "--dryrun"):
            dryrun = True
        elif opt in ("-j", "--json"):
            json_path = arg

    try:
        if not csv_path and not json_path:
            raise Exception("You need to pick one of the intake methods. See -h")
        if csv_path and json_path:
            raise Exception("You can only pick one of the intake methods. See -h")
        if csv_path:
            read_csv(csv_path, dryrun)
        elif json_path:
            read_json(json_path, dryrun)
    except Exception as e:
        print("ERROR: %s" % e)


if __name__ == "__main__":
    main(sys.argv[1:])
