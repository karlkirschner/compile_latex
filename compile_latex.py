#!/usr/bin/env python3
"""
This is a script that can be used to compile a latex document (e.g. filename.tex),
    ensuring that all cross references and citations are correctly displayed. The
    documents are compiled using pdflatex.

Usage: compile_latex.py filename (i.e. minus the .tex extension)
Requirement: pdflatex

Note: the last 'remove_files()' line removes all of the Latex-generated files.

Karl N. Kirschner, Ph.D.
k.n.kirschner@gmail.com

MIT License
"""

import os
import subprocess
import sys


## remove existing Latex-generated files
def remove_files(file_basename=None):
    extensions = ['aux', 'bbl', 'blg', 'log', 'nav', 'out', 'snm',
                  'toc', 'vrb', 'dvi', 'lot', 'lof', 'glo', 'ist',
                  'bcf', 'acn', 'run.xml']
    for ext in extensions:
        if os.path.exists('{0}.{1}'.format(file_basename, ext)):
            os.remove('{0}.{1}'.format(file_basename, ext))


if __name__ == "__main__":

    if len(sys.argv) == 2:  ## requires the command and the input filename

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

    ## remove existing texfile.pdf
    if os.path.exists('{0}.pdf'.format(texfile)):
        os.remove('{0}.pdf'.format(texfile))

    ## sequence of commands
    commands = [
        ['pdflatex', '{0}.{1}'.format(texfile, 'tex')],
        ['bibtex',   '{0}.{1}'.format(texfile, 'aux')],
        ['pdflatex', '{0}.{1}'.format(texfile, 'tex')],
        ['pdflatex', '{0}.{1}'.format(texfile, 'tex')]
        ]

    for compile_tex in commands:
        subprocess.call(compile_tex)

    remove_files(texfile)
