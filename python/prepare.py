#!/usr/bin/env python3
 
import sys

infini = 999;
pointsTo = '';
currentNode = None;
startNode = sys.argv[1];

def emit():
	dist = infini;
	if currentNode == startNode:
		dist = 0;
	print(currentNode + ' ' + str(dist) + ' ' + pointsTo);

for line in sys.stdin:	
	lineValues = line.strip().split('\t');
	nid = lineValues[0];
	neighbor = lineValues[1];
	distance = int(lineValues[2]);

	if currentNode != None:
		if currentNode != nid:
			emit();
			pointsTo = '';
			currentNode = nid;
	else: 
		currentNode = nid;
	pointsTo += neighbor + ',' + str(distance) + ':';

emit();
