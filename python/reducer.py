#!/usr/bin/env python3
 
import sys

minDistance = 9999;
currentMinNode = None;
neighbors = None;
currentNode = None;

def emit(path):
	print(str(currentNode) + ' ' + str(minDistance) + ' ' + neighbors + ' ' + path);

for line in sys.stdin:
	lineValues = line.strip().split(' ');
	nid = int(lineValues[0]);
	type = lineValues[1];
	distance = int(lineValues[2]);

	if type == 'NODE':
		if currentNode != None:
			if currentMinNode == None:
				currentMinNode = nid;
			emit(path);
		path = lineValues[4];
		neighbors = lineValues[3];
		currentNode = nid;
		minDistance = distance;
		currentMinNode = nid;
	else:
		if distance < minDistance:
			minDistance = distance;
			currentMinNode = nid;
			path = lineValues[3];
emit(path);
