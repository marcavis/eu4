#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re, os, tempfile, shutil
#usage: ./tagcheck.py <mod's 00_countries> <vanilla 00_countries>

def main(outgoing, ingoing, filenames):
	outgoing = "".join(codecs.open(outgoing, encoding="utf-8").readlines())
	ingoing = "".join(codecs.open(ingoing, encoding="utf-8").readlines())
	for x in filenames:
		thisFile = "".join(codecs.open(x, encoding="utf-8").readlines())
		#print(thisFile)
		thisFile = thisFile.replace(outgoing, ingoing)
		#print(thisFile)
		newFile = codecs.open(x, 'w', encoding="utf-8")
		newFile.write(thisFile)


if __name__ == "__main__":
	if len(sys.argv) >= 4:
		main(sys.argv[1], sys.argv[2], sys.argv[3:])
	else:
		print("Usage: ./replaceAll.py <file with lines to remove> <file with lines to add> <1 or more files to apply to>")
		print("Make sure all files are of the same newline type.")
