inf = -1

class Graph:
	def __init__(self, n):
		self.n = n
		self.edges = []
		for i in range(n):
			l = []
			for j in range(n):
				l.append(inf)
			self.edges.append(l)
			
	def addEdge(self, u, v, w):
		self.edges[u][v] = w
	
	def printGraph(self):
		for i in range(self.n):
			for j in range(self.n):
				print(self.edges[i][j], end=' ')
			print('')

def Test():
    graph = Graph(5)

    graph.addEdge(0, 1, 1)
    graph.addEdge(0, 2, 3)
    graph.addEdge(1, 2, 2)
    graph.addEdge(2, 3, 7)
    graph.addEdge(3, 4, 9)
    graph.addEdge(4, 0, 4)
    graph.addEdge(4, 2, 5)

    graph.printGraph()

Test()