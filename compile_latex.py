#!/usr/bin/env python3
"""
Script to compile a latex document (e.g. filename.tex)

Usage: compile_latex.py filename (i.e. minus the .tex extension)

Note: you can comment out the last 'remove_files()' line to keep
    all of the generated tex documents. This might be helpful
    if you want to keep the .bbl, .toc, .lot and .lof files.
"""

import glob
import os
import subprocess
import sys


# remove existing Latex generated files
def remove_files(file_basename=None):
    extensions = ['aux', 'bbl', 'blg', 'log', 'nav', 'out', 'snm', 'toc', 'vrb', 'dvi', 'lot', 'lof']
    for ext in extensions:
        if os.path.exists('{0}.{1}'.format(file_basename, ext)):
            os.remove('{0}.{1}'.format(file_basename, ext))


if __name__ == "__main__":

    if len(sys.argv) == 2:  # requires the command and the input filename

        texfile = sys.argv[1]

        if os.path.isfile('{0}.tex'.format(texfile)):
            print(os.path.isfile('{0}.tex'.format(texfile)))
        else:
            print(os.path.isfile('{0}.tex'.format(texfile)))
            raise TypeError("You did not specify a file that exists: '{0}'.".format(texfile))
    else:
        raise TypeError("You did not specify a file to compile.\n\n"
                        "Usage: compile_latex.py filename (i.e. minus the '.tex' extension)\n")

    remove_files(texfile)

    # remove existing pdf of the input
    if os.path.exists(sys.argv[1] + '.pdf'):
        os.remove(sys.argv[1] + '.pdf')

    # sequence of commands needed
    commands = [
        ['pdflatex', sys.argv[1] + '.tex'],
        ['bibtex',   sys.argv[1] + '.aux'],
        ['pdflatex', sys.argv[1] + '.tex'],
        ['pdflatex', sys.argv[1] + '.tex']
        ]

    for compile_tex in commands:
        subprocess.call(compile_tex)

    remove_files(texfile)
