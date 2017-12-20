#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re, os, tempfile, shutil
#usage: ./tagcheck.py <mod's 00_countries> <vanilla 00_countries>

def main():

	files = os.listdir(".")

	regex = re.compile("^[0-9]{4}\.[0-9]+\.[0-9]+")
	for f in files:
		thisFile = codecs.open(f, encoding="utf-8").readlines()
		for line in range(len(thisFile)):
			#if re.search("[0-9]+", line):
			result = regex.search(thisFile[line])
			if result:
				match = result.group(0)
				thisFile[line] = thisFile[line].replace(match, closestDate(match))
		#thisFile = thisFile.replace(outgoing, ingoing)
		newFile = codecs.open(f, 'w', encoding="utf-8")
		newFile.writelines(thisFile)
		#for line in thisFile: print(line)

def closestDate(inputDate):
	dates = [[1467,6,15], [1493,6,9], [1511,9,25], [1523,8,25], [1536,4,7],
	[1546,5,19], [1554,3,1], [1569,10,10], [1582,6,21], [1600,9,13], [1615,1,1]]
	year, month, day = [int(x) for x in inputDate.split(".")]
	for date in dates:
		txtDate = ".".join([str(x) for x in date])
		if year < date[0]:
			return txtDate
		elif year == date[0] and month < date[1]:
			return txtDate
		elif year == date[0] and month == date[1] and day <= date[2]:
			return txtDate
	return inputDate

if __name__ == "__main__":
	main()
