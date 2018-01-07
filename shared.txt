textFile = sc.textFile("data/input.dat")

def customSplitNodesTextFile(node):
	nid, distance, neighbors = node.split(' ')
	neighbors = neighbors.split(':')
	neighbors = neighbors[:len(neighbors) - 1]
	return (nid , (int(distance), neighbors))

def customSplitNodesIterative(node):
	nid = node[0]
	distance = node[1][0]
	neighbors = node[1][1]
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

nodes = textFile.map(lambda node: customSplitNodesTextFile(node));
#nodes.collect()

nodesValues = nodes.map(lambda x: x[1])
neighbors = nodesValues.map(lambda nodeData: map(lambda neighbor: customSplitNeighbor(nodeData[0], neighbor), nodeData[1])).flatMap(lambda x: x)
#neighbors.collect()

mapper = nodes.union(neighbors)
#mapper.collect()

reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))
reducer.collect()

for i in range(6):
	nodes = reducer.map(lambda node: customSplitNodesIterative(node));
	nodesValues = nodes.map(lambda x: x[1])
	neighbors = nodesValues.map(lambda nodeData: map(lambda neighbor: customSplitNeighbor(nodeData[0], neighbor), nodeData[1])).flatMap(lambda x: x)
	mapper = nodes.union(neighbors)
	reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))

reducer.collect()








r = nodes.map(lambda x: x[1][1])
r.map(lambda x: map(lambda x2: bilalSplit(x2), x)).collect()

nodesValues.map(lambda nodeData: map(lambda neighbor: customSplitNeighbor(nodeData[0], neighbor), nodeData[1])).collect().flatMap(lambda x: x)
neighbors = nodesValues.map(lambda nodeData: map(lambda neighbor: customSplitNeighbor(nodeData[0], neighbor), nodeData[1]))
neighbors.collect()

[
(u'1', (0, [u'2,10', u'3,5'])),
(u'2', (999, [u'3,2', u'4,1'])),
(u'3', (999, [u'2,3', u'4,9', u'5,2'])),
(u'4', (999, [u'5,4'])),
(u'5', (999, [u'4,6', u'1,7'])),
[
	(u'2', (10, 'None')), (u'3', (5, 'None'))], [(u'3', (1001, 'None')), (u'4', (1000, 'None'))], [(u'2', (1002, 'None')), (u'4', (1008, 'None')), (u'5', (1001, 'None'))], [(u'5', (1003, 'None'))], [(u'4', (1005, 'None')), (u'1', (1006, 'None'))]]





neighborsData = nodesValues.
neighbors = neighborsData.map(lambda x: customSplitNeighbor(x[0], x[1]))
#neighborsData.collect()

mapper = nodes.union(neighbors)
#mapper.collect()


formatedNeighbors = nodes.map(lambda x: x[1])
#formatedNeighbors.collect()

neighbors = nodes.map(lambda x: splitNeighbors(x[1][0], x[1][1]))
#neighbors.collect()


neighbors = nodes.map(lambda x: x[1][1]).map(lambda x: x.split(':')).flatMap(lambda x: x).filter(lambda x: x != '').map(lambda x: customSplitNeighbors(x))








def minDistance(x, y):
	dist1 = int(x.split('/')[0])
	dist2 = int(y.split('/')[0])
	if dist1 <= dist2:
		return x
	else:
		return y

reducer = mapper.reduceByKey(lambda x, y: minDistance(x, y))


distrange = sc.parallelize(range(0, 100)) // rdd but range(0,100) is list
indeg = sc.broadcast(indegree.collect())
count = indegree.count()
outputResult = distrange.map(lambda x: (x, len(filter(lambda y: y[1]>x, indeg.value))/81306.0))
