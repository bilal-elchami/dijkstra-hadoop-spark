def min_distance((source1, dist1), (source2, dist2)):
	if dist1 <= dist2:
		return (source1, dist1)
	
	else: 
		return (source2, dist2)


inputs = 'data/new-data.dat'
output = 'output'
sourceNode = 1
destinationNode = 4

def customSplit(row):
	firstNode, secondNode, distance = row.split('\t')
	return (int(firstNode), (int(secondNode)), int(distance))

inputForTheProgram = sc.textFile(inputs)
# splittedInput = inputForTheProgram.map(lambda input : input.split(':')).map(lambda (node, edges) : (int(node), map(int, edges.split())))
edges = inputForTheProgram.map(lambda row : customSplit(row))
#print edges.collect()

knownPath = sc.parallelize([(1, ('',0))])


############################################################
####		Instead of the "6" in the for loop			####
############################################################
####	edges.flatMap(lambda x: x).distinct().count()	####
############################################################
for i in range(6):
	print 'joinEdgesWithKnownPath \n'
	joinEdgesWithKnownPath = edges.join(knownPath.filter(lambda (node,(source, dist)) : dist==i))
	joinEdgesWithKnownPath.collect()
	intermediatePath = joinEdgesWithKnownPath.map(lambda (node, (dest, (source, dist))) : (dest, (node, dist+1)))
	print 'intermediatePath \n'
	intermediatePath.collect()
	print 'union \n'
	knownPath.union(intermediatePath).collect()
	knownPath = knownPath.union(intermediatePath).reduceByKey(min_distance)
	print 'knownPath \n'
	knownPath.collect()
	print '\n\n\n'
	# knownPath.saveAsTextFile(output + '/iter-' + str(i))
	
finalPath = [int(destinationNode)]
	
while destinationNode!= sourceNode and destinationNode != '':
	#print destinationNode
	lookUpValue = knownPath.lookup(destinationNode)
	# print lookUpValue
	
	if lookUpValue[0][0] =='':
		break
	else:
		destinationNode = lookUpValue[0][0]
		finalPath.append(destinationNode)

#print finalPath
finalPath = finalPath[::-1]
finalPath = sc.parallelize(finalPath)
#finalPath.saveAsTextFile(output + '/path')
