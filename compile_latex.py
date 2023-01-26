#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def remove_files(file_basename: str):
    ''' Remove latex files other than the TEX and PDF files.'''

    extensions = ['aux', 'bbl', 'blg', 'log', 'nav', 'out', 'snm',
                  'toc', 'vrb', 'dvi', 'lot', 'lof', 'glo', 'ist',
                  'bcf', 'acn', 'run.xml']

    if not isinstance(file_basename, str):
        raise TypeError(f'file_basename (i.e. {file_basename}) was not provided as a string')
    else:
        for ext in extensions:
            if os.path.exists('{0}.{1}'.format(file_basename, ext)):
                os.remove('{0}.{1}'.format(file_basename, ext))


def compile(file_basename: str):
    if os.path.exists('{0}.pdf'.format(inputfile)):
        os.remove('{0}.pdf'.format(inputfile))

    ## sequence of commands
    commands = [['pdflatex', f'{inputfile}.tex'],
                ['bibtex',   f'{inputfile}.aux'],
                ['pdflatex', f'{inputfile}.tex'],
                ['pdflatex', f'{inputfile}.tex']
               ]

    for compile_tex in commands:
       #subprocess.call(compile_tex, stdout=open(os.devnull, 'wb')) ## silent mode
       subprocess.call(compile_tex)


if __name__ == "__main__":
    """ This script that compiles a latex document (e.g. filename.tex) using pdflatex,
        ensuring that all cross references and citations are correctly displayed.

        Usage: compile_latex.py -f filename (i.e. minus the .tex extension) [-d (Y/N)]

        Input:
            inputfile: basename for the LaTeX (e.g. filename)
            delete: option to delete LaTex temporary files 

        Output:
            files normally created when running pdflatex

        Additional Requirement:
            pdflatex
            bibtex

        Author: Karl N. Kirschner, Ph.D.
        E-mail: karl.kirschner@h-brs.de

        MIT License
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--inputfile", type=str, help="LaTeX file to compile.")
    parser.add_argument("-d", "--delete", type=str, help="Delete temporary LaTeX files made? [Y/N]")
    args = parser.parse_args()

    inputfile = args.inputfile
    delete = args.delete

    if not os.path.isfile(f'{inputfile}.tex'):
        raise TypeError(f'You did not specify a file, or it dose not exit that exists.')
    else:

        ## clean up existing files
        remove_files(inputfile)

        compile(inputfile)

        if delete in ['Y', 'y', 'yes']:
            print("\nRemoving LaTeX temporary files.\nDone.")
            remove_files(file_basename=inputfile)