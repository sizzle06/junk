# -*- coding: utf-8 -*-
#
# file : color.py
# brief : This code is script for coloring texts on terminal.
# reference : https://stackoverflow.com/questions/287871/print-in-terminal-with-colors

class color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (color.HEADER + "[" + "HEADER" + "]" + color.ENDC)
print (color.OKBLUE + "[" + "OKBLUE" + "]" + color.ENDC)
print (color.OKGREEN + "[" + "OKGREEN" + "]" + color.ENDC)
print (color.WARNING + "[" + "WARNING" + "]" + color.ENDC)
print (color.FAIL + "[" + "FAIL" + "]" + color.ENDC)
print (color.BOLD + "[" + "BOLD" + "]" + color.ENDC)
print (color.UNDERLINE + "[" + "UNDERLINE" + "]" + color.ENDC)
