#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random, sys, codecs, re

#iaponia tradegood colors here

def distance(c, d):
    return (d[0] - c[0]) ** 2 + (d[1] - c[1]) ** 2 + (d[2] - c[2]) ** 2

def main(_file, colorFloats = True):
    lines = codecs.open(_file).readlines()
    if colorFloats:
        lines = [re.findall(r'\d+.?\d*', line) for line in lines if "color" in line]
        lines = [[float(line[0]), float(line[1]), float(line[2])] for line in lines ]
    else:
        lines = [re.findall(r'\d+', line) for line in lines if "color" in line]
        lines = [[float(line[0])/256, float(line[1])/256, float(line[2])/256] for line in lines]
    print(lines)
    newColors = []
    for c in range(30):
        x = [round(random.random(), 2), round(random.random(), 2), round(random.random(), 2)]
        newColors.append((x, min([round(distance(x,d), 4) for d in lines])))

    newColors.sort(key=lambda x: x[1])
    for line in newColors:
        if colorFloats:
            print(line)
        else:
            print(int(line[0][0]*256), int(line[0][1]*256), int(line[0][2]*256), line[1])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--256":
            main(sys.argv[2], False)
    else:
        print("Usage: ./colorstudy.py <file with color definitions> or,")
        print("for colors defined from 0 to 255 instead of 0 to 1,")
        print("./colorstudy.py --256 <file with color definitions>")
