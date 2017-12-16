#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, sys, re, os, tempfile, shutil
#usage: ./tagcheck.py <mod's 00_countries> <vanilla 00_countries>

def main(spreadsheet="changes.csv", provFolder=".", mode="update"):
	sheet = codecs.open(spreadsheet, encoding="utf-8").readlines()
	sheet = [x.strip().split(";") for x in sheet]
	#print(provinces)
	header = sheet[0]
	entries = {x[0]: x[1:] for x in sheet[1:]}
	regexes = [(field + '\s*=.*', field + ' = ') for field in header[1:]]

	files = {f.replace(" ","").split("-")[0]: f for f in os.listdir(provFolder)}

	for field in range(len(header[1:])):
		for e in entries:
			fh, abs_path = tempfile.mkstemp()
			with os.fdopen(fh,'w') as new_file:
				with open(files[e]) as old_file:
					if mode == "update":
						for line in old_file:
							if (field < len(entries[e]) and len(entries[e][field].strip()) > 0):
								new_file.write(re.sub(regexes[field][0], regexes[field][1] + entries[e][field], line))
							else:
								new_file.write(line)
					elif mode == "add":
						new_file.write(header[field + 1] + " = " + entries[e][field])
						for line in old_file:
							new_file.write(line)
			#Remove original file
			os.remove(files[e])
			#Move new file
			shutil.move(abs_path, files[e])

if __name__ == "__main__":
	if len(sys.argv) == 1:
		main()
	elif len(sys.argv) == 2:
		main(sys.argv[1])
	elif len(sys.argv) == 3:
		main(sys.argv[1], sys.argv[2])
	else:
		print("Run this on a folder with a semicolon-separated file called changes.csv")
		print("With parameters: ./batchedit.py <csv file, separated by ; semicolons, with province IDs and tradegoods>")
