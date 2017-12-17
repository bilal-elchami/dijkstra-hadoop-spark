#!/usr/bin/env python3
 
import sys

minDistance = 9999;
neighbors = None;
currentNode = None;

for line in sys.stdin:
	lineValues = line.strip().split(' ');
	nid = int(lineValues[0]);
	type = lineValues[1];
	distance = int(lineValues[2]);

	if type == 'NODE':
	    if currentNode != None:
    		print(str(currentNode) + ' ' + str(minDistance) + ' ' + neighbors);
	    neighbors = lineValues[3];
	    currentNode = nid;
	    minDistance = distance;
	else:
		if distance < minDistance:
			minDistance = distance;

print(str(currentNode) + ' ' + str(minDistance)+ ' ' + neighbors);
