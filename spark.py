textFile = sc.textFile("data/input.dat")

count = sc.accumulator(0)

def customSplitNodesTextFile(node):
	if len(node.split(' ')) < 3:
		nid, distance = node.split(' ')
		neighbors = None
	else:
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
	if neighbor!=None:
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
		count.add(1);
		distance = dist2
		path = nodeValue2[2]
	return (distance, neighbors, path)

def formatResult(node):
	nid = node[0]
	minDistance = node[1][0]
	path = node[1][2]
	return nid, minDistance, path

nodes = textFile.map(lambda node: customSplitNodesTextFile(node))

oldCount = 0
iterations = 0
while True:
	iterations += 1
	nodesValues = nodes.map(lambda x: x[1])
	neighbors = nodesValues.filter(lambda nodeDataFilter: nodeDataFilter[1]!=None).map(
		lambda nodeData: map(
			lambda neighbor: customSplitNeighbor(
				nodeData[2], nodeData[0], neighbor
			), nodeData[1]
		)
	).flatMap(lambda x: x)
	mapper = nodes.union(neighbors)
	reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))
	nodes = reducer.map(lambda node: customSplitNodesIterative(node))
	nodes.count() # We call the count to execute all the RDD transformations
	if oldCount == count.value:
		break
	oldCount=count.value

print('Finished after: ' + str(iterations) + ' iterations')
result = reducer.map(lambda node: formatResult(node))
