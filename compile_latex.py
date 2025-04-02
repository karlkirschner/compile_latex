#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def remove_files(file_basename: str):
    """Remove LaTeX files other than the TEX and PDF files."""

    extensions = ['.aux', '.acn', '.bbl', '.bcf', '.blg',
                  '.dvi', '.glo', '.idx', '.ilg', '.ind',
                  '.ist', '.lof', '.log', '.lot', '.nav',
                  '.out', '.snm', '.spl', '.toc', '.vrb',
                  '.run.xml', '-blx.bib'
                  ]

    if not isinstance(file_basename, str):
        raise TypeError(f'file_basename (i.e. {file_basename}) must be a string')
    else:
        for ext in extensions:
            file_path = f'{file_basename}{ext}'
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                except OSError as error:
                    print(f'Error removing {file_path}: {error}')


def compile_latex(file_basename: str, bib: bool):
    """Compile the LaTeX document."""

    if os.path.exists(f'{file_basename}.pdf'):
        try:
            os.remove(f'{file_basename}.pdf')
        except OSError as error:
            print(f'Error removing existing PDF: {error}')

    if bib:
        commands = [['pdflatex', f'{file_basename}.tex'],
                    ['bibtex',   f'{file_basename}.aux'],
                    ['pdflatex', f'{file_basename}.tex']]
    else:
        commands = [['pdflatex', f'{file_basename}.tex'],
                    ['pdflatex', f'{file_basename}.tex']]

    for command in commands:
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as error:
            print(f'Error executing command {command}: {error}')
            sys.exit(1)


def main():
    """Main function to parse arguments and compile the LaTeX document."""

    parser = argparse.ArgumentParser(description="Compile a LaTeX document.")
    parser.add_argument('inputfile', help='LaTeX file to compile (without .tex extension).')
    parser.add_argument('-b', '--bibtex', action='store_false', help='LaTeX file does NOT uses a bibtex file.')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete temporary LaTeX files.')
    args = parser.parse_args()

    inputfile = args.inputfile

    if not inputfile.endswith(".tex"):
        print("Error: Input file must end with '.tex'.")
        sys.exit(1)
    elif not os.path.isfile(inputfile):
        print(f"Error: File '{inputfile}' does not exist.")
        sys.exit(1)
    else:
        file_basename = os.path.splitext(inputfile)[0] #Extract basename

        compile_latex(file_basename=file_basename, bib=args.bibtex)

        if args.delete:
            remove_files(file_basename)
            print('\nRemoved LaTeX temporary files.\nDone.')

if __name__ == "__main__":
    """ This script compiles a latex document using pdflatex, ensuring that all
        cross references and citations are correctly displayed.

    Usage: compile_latex.py filename.tex [-d]

    Input:
        inputfile: basename for the LaTeX (e.g. filename)
        -d: delete LaTeX temporary files 

    Output:
        files normally created when running pdflatex

    Additional Requirement:
        pdflatex
        bibtex

    Author: Karl N. Kirschner, Ph.D.
    E-mail: karl.kirschner@h-brs.de

    MIT License
"""
    main()
