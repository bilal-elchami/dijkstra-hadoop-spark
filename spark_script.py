textFile = sc.textFile("data/input.dat")

sourceNode = 'A'
targetNode = 'F'

def splitInput(row):
	currentSourceNode, targetNode, distance = row.split('\t')
	return (currentSourceNode, targetNode, float(distance))


data = textFile.map(lambda row: splitInput(row))
#data.collect()

allNodes = data.flatMap(lambda row: (row[0],row[1])).distinct()
#allNodes.collect()

def setVertexDistance(node):
	if node == sourceNode:
		return (node, 0.0)
	else:
		return (node, 999)

vertex = allNodes.map(lambda node: setVertexDistance(node))
# vertex.collect()