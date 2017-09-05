#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess, scipy.misc, numpy
#usage: ./tagcheck.py <mod's 00_countries.txt> <vanilla's 00_countries.txt>

def main():
	provinces = codecs.open("definition.csv", encoding="latin_1").readlines()
	provinces = [x.strip().split(";") for x in provinces[1:]]
	#simpleProvList = []
	print("graph \"grafo\" {\nnode [width=0.5,height=0.5];\n" )
	i = 1
	for p in provinces:
		#simpleProvList.append([int(p[1]), int(p[2]), int(p[3])])
		print("N" + str(i) + " [label=\""+p[4]+"\",fontsize=10];")
		i+=1
	edgeList = []

	subprocess.check_output(['convert', 'provinces.bmp', 'provinces-temp.png'])
	provMap = scipy.misc.imread('provinces-temp.png')
	colorMap = {}
	for line in range(1999, len(provMap)-1):
		#if line%50 == 0:
		#	print("line", line, "of", len(provMap))
		for col in range(1, len(provMap[0])-1):
			for n in neighbors(line, col):
				if numpy.any(provMap[line, col] != provMap[n[0], n[1]]):
					#print ((provMap[line, col], provMap[n[0], n[1]])) not in edgeList
					#if ((provMap[line, col][:2], provMap[n[0], n[1]][:2])) not in edgeList:
					this = provMap[line, col]
					this = [int(x) for x in this[:3]]
					that = provMap[n[0], n[1]]
					that = [int(x) for x in that[:3]]
					if (this, that) not in edgeList and (that, this) not in edgeList:
						edgeList.append((this, that))
						#print(this,that)


	for edge in edgeList:
		print("N"+str(findProv(edge[0], provinces))+ " -- N" +
		 str(findProv(edge[1], provinces)) + " [weight=1,style=\"setlinewidth(1.0)\"];")
	#s.index([x for x in s if x[1:] == [2,3,2]][0])
	print("}")

	# subprocess.check_output(['convert', 'provinces-numbered.png', '-scale', '200%', 'provinces-numbered.png'])
	# numbers = ['convert', 'provinces-numbered.png', '-font', 'FreeSans-Bold', '-pointsize','20']
	# for prov in provinces:
	# 	if (int(prov[1]), int(prov[2]), int(prov[3])) in colorMap.keys():
	# 		thisColor = colorMap[(int(prov[1]), int(prov[2]), int(prov[3]))]
	# 		y = sum([c[0] for c in thisColor])//len(thisColor) * 2
	# 		x = abs(sum([c[1] for c in thisColor])//len(thisColor) *2)
	# 		colorOnCenter = provMap[y/2][x/2]
	# 		if (colorOnCenter[0], colorOnCenter[1], colorOnCenter[2]) != (int(prov[1]), int(prov[2]), int(prov[3])):
	# 			y, x = sorted(thisColor, key=lambda point: distance((point[0]*2, point[1]*2), (y, x)))[0]
	# 			y, x = y*2, x*2
	# 		if len(thisColor) > 400:
	# 			numbers += ['-pointsize', '16']
	# 		else:
	# 			numbers += ['-pointsize', '10']
	# 		numbers += ['-draw', "fill white text "+str(x-4)+","+str(y+4)+" '"+prov[0]+"'"]
	# 		numbers += ['-draw', "fill black text "+str(x-3)+","+str(y+3)+" '"+prov[0]+"'"]

	subprocess.check_output(['rm', 'provinces-temp.png'])

def findProv(color, provList):
	return [p[0] for p in provList if color[0] == int(p[1])
	and color[1] == int(p[2]) and color[2] == int(p[3])][0]

def distance(x, y):
	return((x[0]-y[0])**2 + (x[1]-y[1])**2)
	#no need to take the square root

def neighbors(x, y):
	return ((x-1, y),(x+1, y),(x,y-1),(x,y+1))

if __name__ == "__main__":
	main()
