from graph import Graph


test = Graph()
test.addNode(1)
test.addNode(2)
test.addNode(3)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(1,3)
test.addNode(4)
test.addNode(5)
test.addNode(6)
test.printIncidence()
print("\n\n")
test.printAdjency()

if test.Warshall_Connectivity():
	print("Connected graph")
else:
	print("Disconnected graph")

if not test.Regular_graph() :
	print("Not regular")

test.Isolated_nodes()