#! /usr/bin/env python3
from os.path import isdir,isfile
from sys import argv
OUTGROUP_SUBSTRINGS = {
    '|camel|',
}

# check args
if len(argv) != 3:
    print("USAGE: %s <input_fasta> <output_outgroup_list>" % argv[0]); exit(1)
if not isfile(argv[1]):
    raise ValueError("Invalid input FASTA file: %s" % argv[1])
if isfile(argv[2]) or isdir(argv[2]):
    raise ValueError("Output file exists: %s" % argv[2])

# parse data and write
out = open(argv[2], 'w')
for l in open(argv[1]):
    if not l.startswith('>'):
        continue
    og = False
    for pre in OUTGROUP_SUBSTRINGS:
        if pre in l:
            og = True; break
    if og:
        out.write(l.strip()[1:]); out.write('\n')
out.close()
