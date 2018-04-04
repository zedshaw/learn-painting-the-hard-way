import os
from slugify import slugify
import re

regex = re.compile(r"\* ([0-9][0-9]): ([A-Za-z0-9, ]+)(\-\- )?(.*$)?")

outline = (x.strip() for x in open("outline.txt").readlines())
exercises = (regex.match(x).groups() for x in outline if x.startswith("*"))

main_index_rst = open("index.rst", "w")
main_title = "Learn Painting The Hard Way"
main_index_rst.write("=" * len(main_title))
main_index_rst.write("\n")
main_index_rst.write(main_title)
main_index_rst.write("\n")
main_index_rst.write("=" * len(main_title))
main_index_rst.write("\n")

for groups in exercises:
    num, title, _, pyfile = groups

    fname = "ex%s-%s" % (num, slugify(title.decode("utf-8")))
    if not os.path.exists(fname):
        os.mkdir(fname)
        os.mkdir(fname + "/photos")
        os.mkdir(fname + "/pastels")
        os.mkdir(fname + "/lectures")
        os.mkdir(fname + "/demos")

    with open("%s/index.rst" % (fname), 'w') as index:
        full_title = "Exercise %s: %s" % (num, title)
        dashes = "=" * len(full_title) 
        index.write("""%s\n%s\n""" % (full_title, dashes))

    main_index_rst.write("* Exercise %s: %s <%s/index.html>\n" % (num, title, fname))
