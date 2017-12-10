#!/usr/bin/env python3
 
import sys

startingNode = 'A';
endNode = 'F';
nodes = [];
vertex = [];

def getVertexDistance(node):
	if node == startingNode:
		return (node, 0.0)
	else:
		return (node, 999)

# check wether the node is already added in the list nodes
def containsList(node):
    for i in range(len(nodes)):
        if nodes[i] == node:
            return True
    return False

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip().split('\t');
	sourceNode = line[0];
	targetNode = line[1];
	distance = line[2];
	if not containsList(sourceNode): 
		nodes.append(sourceNode)
	if not containsList(targetNode):
		nodes.append(targetNode)
	print(sourceNode, '--', distance, '-->', targetNode);


def setVertex():
    for i in range(len(nodes)):
        vertex.append(getVertexDistance(nodes[i]))
        print(vertex[i])

setVertex()
