from datetime import datetime
from pathlib import Path
import os


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


def new_term(term, definition, link=None, slug=None, dryrun=False):
    this_file = Path(os.path.realpath(__file__))
    bin_dir = this_file.parent.parent
    content_dir = os.path.join(bin_dir.parent, "content")

    if slug:
        base_name = slug.lower()
    else:
        base_name = term.lower()
        base_name = base_name.replace(" ", "-")
    filename = base_name + ".md"

    if "/" in filename:
        raise Exception("Filename has an '/' in it, use a slug without '/' to "
                        "override for term '%s'" % term)

    md_file = os.path.join(content_dir, filename)
    if os.path.exists(md_file):
        raise Exception("file already exists: %s" % filename)

    print("'%s'" % term)
    print("  - '%s'" % definition)
    if link:
        print("  - '%s'" % link)

    if dryrun:
        print("  - dryrun: would have created %s" % md_file)
        return

    content = file_content(term, definition, link, slug)
    with open(md_file, 'w') as f:
        f.write(content)

    print("  - Created %s" % md_file)
