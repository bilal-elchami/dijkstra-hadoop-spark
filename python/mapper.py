#!/usr/bin/env python3

import sys

for line in sys.stdin:
	lineValues = line.strip().split(' ')
	nid = lineValues[0]
	distance = int(lineValues[1])
	neighbors = 'no-neighbors'
	if len(lineValues) > 2:
		neighbors = lineValues[2]
	path = nid
	if len(lineValues) > 3:
		path = lineValues[3]
		elements = path.split('->')
		if elements[len(elements) - 1] != nid:
			path = lineValues[3] + '->' + nid
	print(nid + ' NODE ' + str(distance) + ' ' + neighbors + ' ' + str(path));

	if neighbors != 'no neighbors':
		adjacencyList = neighbors.split(':')
		for i in range(len(adjacencyList) - 1):
			neighborData = adjacencyList[i].split(',')
			neighbor = neighborData[0]
			currentPath = path + '->' + neighbor
			neighborDistance = distance + int(neighborData[1])
			print(neighbor + ' VALUE ' +  str(neighborDistance) + ' ' + currentPath)
