class EdgeNode:
	def __init__(self, v, w):
		self.vertex = v
		self.weight = w

class VertexNode:
	def __init__(self, v):
		self.vertex = v
		self.edges = []

class Graph:
	def __init__(self, n):
		self.n = n
		self.nodes = [VertexNode(i) for i in range(n)]

	def addEdge(self, u, v, w):
		self.nodes[u].edges.append( EdgeNode(v, w) )
	
	def printGraph(self):
		for i in range(self.n):
			print("Vertex ", i, end=':')
			for edge in self.nodes[i].edges:
				print(  edge.vertex, '(', edge.weight, ')', end=' ')
			print('')
				
def Test():
    graph = Graph(5)

    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 2, 2)
    graph.addEdge(1, 2, 3)
    graph.addEdge(2, 3, 4)
    graph.addEdge(3, 4, 2)

    graph.printGraph()

Test()