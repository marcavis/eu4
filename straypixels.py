#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs, sys, re, subprocess, scipy.misc, numpy

def main():
	subprocess.check_output(['convert', 'provinces.bmp', 'provinces-temp.png'])
	provMap = scipy.misc.imread('provinces-temp.png')
	colorMap = {}
	for line in range(1, len(provMap)-1):
		if line % 100 == 0:
			print(line)
		#if line%50 == 0:
		#	print("line", line, "of", len(provMap))
		for col in range(1, len(provMap[0])-1):
			different = 0
			for n in neighbors(line, col):
				if numpy.any(provMap[line, col] != provMap[n[0], n[1]]):
					different += 1
			if different == 4:
				print("Stray pixel at x:", col, "y:", line, "found!")


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
