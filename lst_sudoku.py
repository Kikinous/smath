#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="sudoku.tex"

myRequest.ok_filenames_list=["e_smath"]
#myRequest.ok_filenames_list.append("0370_ap")
