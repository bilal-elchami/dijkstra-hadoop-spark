textFile = sc.textFile("data/input.dat")

def customSplitNodesTextFile(node):
	nid, distance, neighbors = node.split(' ')
	neighbors = neighbors.split(':')
	neighbors = neighbors[:len(neighbors) - 1]
	path = nid
	return (nid , (int(distance), neighbors, path))

def customSplitNodesIterative(node):
	nid = node[0]
	distance = node[1][0]
	neighbors = node[1][1]
	path = node[1][2]
	elements = path.split('->')
	if elements[len(elements) - 1] != nid:
		path = path + '->' + nid;
	return (nid , (int(distance), neighbors, path))

def customSplitNeighbor(parentPath, parentDistance, neighbor):
	nid, distance = neighbor.split(',')
	distance = parentDistance + int(distance)
	path = parentPath + '->' + nid
	return (nid, (int(distance), 'None', path))

def minDistance(nodeValue1, nodeValue2):
	neighbors = None
	distance = 0
	path = ''
	if nodeValue1[1] != 'None':
		neighbors = nodeValue1[1]
	else:
		neighbors = nodeValue2[1]
	dist1 = nodeValue1[0]
	dist2 = nodeValue2[0]
	if dist1 <= dist2:
		distance = dist1
		path = nodeValue1[2]
	else:
		distance = dist2
		path = nodeValue2[2]
	return (distance, neighbors, path)


nodes = textFile.map(lambda node: customSplitNodesTextFile(node));
#nodes.collect()

nodesValues = nodes.map(lambda x: x[1])
neighbors = nodesValues.map(
	lambda nodeData: map(
		lambda neighbor: customSplitNeighbor(
			nodeData[2], nodeData[0], neighbor
		), nodeData[1]
	)
).flatMap(lambda x: x)
#neighbors.collect()

mapper = nodes.union(neighbors)
#mapper.collect()

reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))
reducer.collect()

for i in range(6):
	nodes = reducer.map(lambda node: customSplitNodesIterative(node));
	nodesValues = nodes.map(lambda x: x[1])
	neighbors = nodesValues.map(
		lambda nodeData: map(
			lambda neighbor: customSplitNeighbor(
				nodeData[2], nodeData[0], neighbor
			), nodeData[1]
		)
	).flatMap(lambda x: x)
	mapper = nodes.union(neighbors)
	reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))

reducer.collect()
