import sys


class Graph(object):

	INT_MAX = sys.maxsize 

	def __init__(self, size = 60):
		try:
			self.adjency_matrix = [[0 for x in range(size)] for y in range(size)] 
			self.incidence_matrix = [[0 for x in range(size)] for y in range(size)] 
			self.adjency_matrix[0][0] = 0
			self.incidence_matrix[0][0] = 0
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
			self.adjency_matrix[first_node][second_node] = int(wight)
			self.adjency_matrix[second_node][first_node] = int(wight)
			self.incidence_matrix[first_node][self.edge_size] = int(wight)
			self.incidence_matrix[second_node][self.edge_size] = int(wight)
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

	def Isolated_nodes(self):
		nodes_edge_number = 0
		izolated = True
		print("Isolated nodes: ", end = ' ')
		for index_i in range(1,self.size):
			izolated = True

			for index_j in range(1,self.size):
				
				if self.adjency_matrix[index_i][index_j] != 0:

					izolated = False
					pass
			
			if izolated:		
				print(self.adjency_matrix[index_i][0], end = ', ' )
		print()

	def Warshall_Connectivity(self):

		T_matrix = [[0 for x in range(self.size)] for y in range(self.size)] 
		
		for	index_i in range(1, self.size):
			for index_j in range(1, self.size):

				if(self.adjency_matrix[index_i][index_j] != 0):
					T_matrix[index_i][index_j] = int(self.adjency_matrix[index_i][index_j])
					pass
				
				else:
					T_matrix[index_i][index_j] = self.INT_MAX
					pass

		for	index_k in range(1, self.size):
			for index_i in range(1, self.size):
				for index_j in range(1, self.size):
										
					if((T_matrix[index_i][index_k] + T_matrix[index_k][index_j]) < T_matrix[index_i][index_j]):

						T_matrix[index_i][index_j] = T_matrix[index_i][index_k] + T_matrix[index_k][index_j]

		for	index_i in range(1, self.size):
			for index_j in range(1, self.size):
				if(T_matrix[index_i][index_j] == self.INT_MAX):
					return False
		return True

	def Regular_graph(self):
		index_j = 1
		first_nodes_edge_number = 0
		nodes_edge_number = 0
		index_i = 2
		for index_i in range(1, self.size):
			if self.adjency_matrix[1][index_i] != 0:
				first_nodes_edge_number += 1

		while( index_i <= self.size ):
			while( index_j <= self.size):
				
				if self.adjency_matrix[index_i][index_j] != 0:
					nodes_edge_number += 1
					pass

				index_j += 1
			index_i += 1
			if(first_nodes_edge_number != nodes_edge_number):
				return False
		print(str(nodes_edge_number) + "-regular graph ")
		return True