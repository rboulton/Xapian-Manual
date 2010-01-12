#!/usr/bin/env python

import os
import shutil
import subprocess
import sys

sources = (
    "intro",
    "databases",
    "documents",
    "searches",
    "customsearches",
    "indexstrategy",
    "facets",
    "future",
)

def generate(sources, outdir):
    srcdir = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))
    sources = tuple(os.path.join(srcdir, 'src', source) + '.but'
                    for source in sources)

    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.mkdir(outdir)
    os.chdir(outdir)

    cmd = ["halibut"]
    cmd.extend(sources)

    subprocess.call(cmd)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        outdir = sys.argv[1]
    else:
        outdir = "output"

    generate(sources, outdir)
