#!/usr/bin/env python

import os
import shutil
import subprocess

sources = (
    "intro",
    "databases",
    "documents",
    "searches",
    "customsearches",
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
    generate(sources, "output")
