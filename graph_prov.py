#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess, scipy.misc, numpy

def main():
	output = ""
	provinces = codecs.open("definition.csv", encoding="latin_1").readlines()
	provinces = [x.strip().split(";") for x in provinces[1:]]
	#simpleProvList = []
	output += "graph \"grafo\" {\nnode [width=0.5,height=0.5];\n"

	edgeList = []

	subprocess.check_output(['convert', 'provinces.bmp', 'provinces-temp.png'])
	provMap = scipy.misc.imread('provinces-temp.png')
	colorMap = {}
	for line in range(1, len(provMap)-1):
		print(line)
		#if line%50 == 0:
		#	print("line", line, "of", len(provMap))
		for col in range(1, len(provMap[0])-1):
			for n in twoNeighbors(line, col):
				if numpy.any(provMap[line, col] != provMap[n[0], n[1]]):
					#print ((provMap[line, col], provMap[n[0], n[1]])) not in edgeList
					#if ((provMap[line, col][:2], provMap[n[0], n[1]][:2])) not in edgeList:
					this = provMap[line, col]
					this = [int(x) for x in this[:3]]
					this = findProv(this, provinces)
					that = provMap[n[0], n[1]]
					that = [int(x) for x in that[:3]]
					that = findProv(that, provinces)
					wastes = ["686", "687","688","689","690","691","692","693","694"]
					if int(this) < 750 and int(that) < 750 and this not in wastes and that not in wastes and (this, that) not in edgeList and (that, this) not in edgeList:
						edgeList.append((this, that))
						print(this,that)


	#i = 1
	for x in provinces[:750]:
		if (len([y for y in edgeList if y[0] == x[0]]) > 0 or
		len([y for y in edgeList if y[1] == x[0]]) > 0):
			output += "N" + str(x[0]) + " [label=\""+x[4]+"\",fontsize=10];\n"
			print(x[4])
		else:
			print(x[0])

	for edge in edgeList:
		#print(len(edge[0]), len(edge[1]))
		output += "N"+str(edge[0])+ " -- N"
		output += str(edge[1]) + " [weight=1,style=\"setlinewidth(1.0)\"];\n"
	#s.index([x for x in s if x[1:] == [2,3,2]][0])
	output += "}\n"
	f = open('output.dot', 'w')
	f.write(output)
	f.close()

	subprocess.check_output(['rm', 'provinces-temp.png'])

def findProv(color, provList):
	for p in provList:
		if color[0] == int(p[1]) and color[1] == int(p[2]) and color[2] == int(p[3]):
			return p[0]

def distance(x, y):
	return((x[0]-y[0])**2 + (x[1]-y[1])**2)
	#no need to take the square root

def neighbors(x, y):
	return ((x-1, y),(x+1, y),(x,y-1),(x,y+1))

def twoNeighbors(x, y):
	#return only the preceding pixels to the left and up;
	#sufficient to find borders
	return((x-1, y),(x, y-1))

if __name__ == "__main__":
	main()
