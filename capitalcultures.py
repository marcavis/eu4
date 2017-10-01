#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re, os
#must be at the top-level folder ?

def main(countries, provinces):
	capitalRegex = re.compile('capital = \d+')
	#aareaRegex = re.compile('[a-z|_]*')
	myareas = codecs.open(areaFile, encoding="utf-8").readlines()
	myareas = [x.strip() for x in myareas if '#' not in x]
	myareas = "".join(myareas)
	myareas = myareas.replace("\t"," ")
	myareas = myareas.replace("}","}\n")
	myareas = myareas.split("\n")
	#print myareas

if __name__ == "__main__":
	if len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print("USAGE: ./capitalcultures.py <history/countries folder> <history/provinces folder>")
