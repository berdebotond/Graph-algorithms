from graph import Graph


test = Graph()
test.addNode(1)
test.addNode(2)
test.addNode(3)
test.addNode(4)
test.addNode(5)
test.addEdge(1,2)
test.addEdge(3,4)
test.printIncidence()
print("\n\n")
test.printAdjency()
if test.Warshall_Connectivity():
	print("connected")
else:
	print("disconnected")