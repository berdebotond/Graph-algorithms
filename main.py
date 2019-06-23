from graph import Graph


test = Graph()
test.addNode(1)
test.addNode(2)
test.addNode(3)
test.addEdge(1,2)
test.addEdge(2,3)
test.addEdge(1,3)
test.printIncidence()
print("\n\n")
test.printAdjency()

if test.Warshall_Connectivity():
	print("connected graph")
else:
	print("disconnected graph")

if not test.Regular_graph() :
	print("not regular")
