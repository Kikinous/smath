#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools
import commun

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="automatedChapter.tex"


pythagore=commun.OneChapter("Égalité de Pythagore","4Aexercices.tex")
pythagore.write_the_file()

myRequest.add_plugin(pythagore.set_filename,"medicament")
myRequest.ok_filenames_list=pythagore.ok_filenames_list()
