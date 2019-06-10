class Graph(object):

	def __init__(self, size = 60):
		try:
			self.adjency_matrix = [[0 for x in range(size)] for y in range(size)] 
			self.incidence_matrix = [[0 for x in range(size)] for y in range(size)] 
			self.adjency_matrix[0][0] = 'x'
			self.incidence_matrix[0][0] = 'x'
			self.size = 1
			self.edge_size = 1
			pass
		except Exception as e:
			print("Error :" + e)


		pass 

	def addNode(self, name = 1):
		try:
			self.adjency_matrix[0][name] = name
			self.adjency_matrix[name][0] = name
			self.incidence_matrix[self.size][0] = name
			self.size += 1;
					
			pass
		except Exception as e:
			print("Error" + e)

		pass

	def addEdge(self, first_node, second_node, wight = 1):
		try:
			self.adjency_matrix[first_node][second_node] = wight
			self.incidence_matrix[first_node][self.edge_size] = wight
			self.incidence_matrix[second_node][self.edge_size] = -wight
			self.incidence_matrix[0][self.edge_size] = self.edge_size
			self.edge_size += 1

			pass

		except Exception as e:
			print("Error" + e)

		pass
	
	def printAdjency(self):
		print("Adjency matrix")
		for	indexi in range(0, self.size):
			for indexj in range(0, self.size):
				print(self.adjency_matrix[indexi][indexj], end= ' ')
			print()

		pass

	def printIncidence(self):
		print("Incidence matrix")
		for	indexi in range(0, self.size):
			for indexj in range(0, self.edge_size):
				print(self.incidence_matrix[indexi][indexj], end= ' ')
			print()		
		pass

