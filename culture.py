#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re, os
#must be at the top-level folder ?

def main(areaFile, provFolder, areaToUpdate, newCulture):
	areaRegex = re.compile('[a-z|_]*_area = {[\w\s]+}')
	#aareaRegex = re.compile('[a-z|_]*')
	myareas = codecs.open(areaFile, encoding="utf-8").readlines()
	myareas = [x.strip() for x in myareas if '#' not in x]
	myareas = "".join(myareas)
	myareas = myareas.replace("\t"," ")
	myareas = myareas.replace("}","}\n")
	myareas = myareas.split("\n")
	#print myareas

	myAreaList = {}
	for x in myareas:
		matched = areaRegex.match(x)
		if matched:
			areaAndName = matched.group(0).split('=')
			myAreaList[areaAndName[0].strip()] = areaAndName[1].strip().replace("{","").replace("}","").split(" ")
	#for x in myAreaList:
	#	print x, myAreaList[x]
	
	if '_area' not in areaToUpdate:
		areaToUpdate = areaToUpdate + '_area'
	#print areaToUpdate
	
	for x in myAreaList[areaToUpdate]:
		provRegex = re.compile(str(x)+' ?- ?')
		for _file in os.listdir(provFolder):
			if provRegex.match(_file):
				command = "sed -i -E -- 's/culture = [a-z|-|_]+/culture = " + newCulture + "/g' " + provFolder + _file 
				os.system(command)
	
	#provRegex = re.compile('[0-9]+ ?- ?')
	#for z in range(1, 2800):
	#	provRegex = re.compile(str(z)+' ?- ?')
	#	for _file in os.listdir(provFolder):
	#		if provRegex.match(_file):
	#			print _file
	
if __name__ == "__main__":
	if len(sys.argv) == 5:
		main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
	else:
		print("USAGE: ./culture.py area.txt <history/provinces folder> area culture")
