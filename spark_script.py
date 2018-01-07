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










textFile = sc.textFile("data/input.dat")

def customSplitNodes(node):
	nid, distance, neighbors = node.split(' ')
	neighbors = neighbors.split(':')
	neighbors = neighbors[:len(neighbors) - 1]
	return (nid , (int(distance), neighbors))

def customSplitNeighbor(parentDistance, neighbor):
	nid, distance = neighbor.split(',')
	distance = parentDistance + int(distance)
	return (nid, (int(distance), 'None'))

def minDistance(nodeValue1, nodeValue2):
	dist1 = nodeValue1[0]
	dist2 = nodeValue2[0]
	neighbors = None
	distance = 0
	if nodeValue1[1] != 'None':
		neighbors = nodeValue1[1]
	else:
		neighbors = nodeValue2[1]
	if dist1 <= dist2:
		distance = dist1
	else:
		distance = dist2
	return (distance, neighbors)

nodes = textFile.map(lambda x: customSplitNodes(x));
#nodes.collect()

nodesValues = nodes.map(laWmbda x: x[1])
neighbors = nodesValues.map(lambda nodeData: map(lambda neighbor: customSplitNeighbor(nodeData[0], neighbor), nodeData[1])).flatMap(lambda x: x)
#neighbors.collect()

mapper = nodes.union(neighbors)
#mapper.collect()

reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))
#reducer.collect()
