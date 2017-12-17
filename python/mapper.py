#!/usr/bin/env python3
 
import sys

for line in sys.stdin:
	lineValues = line.strip().split(' ');
	nid = lineValues[0];
	distance = int(lineValues[1]);
	neighbors = lineValues[2];

	print(nid + ' NODE ' + str(distance) + ' ' + neighbors);
	
	adjacencyList = neighbors.split(':');
	for i in range(len(adjacencyList) - 1):
		neighborData = adjacencyList[i].split(',');
		neighbor = neighborData[0];
		neighborDistance = distance + int(neighborData[1]);
		print(neighbor + ' VALUE ' +  str(neighborDistance));
