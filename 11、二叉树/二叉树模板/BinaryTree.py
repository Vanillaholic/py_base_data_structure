class TreeNode:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Tree:
	def __init__(self, maxNodes):
		self.root = None
		self.nodes = [TreeNode() for i in range(maxNodes)]
		self.nodeSize = maxNodes
	
	def GetTreeNode(self, id):
		return self.nodes[id]
	
	def visit(self, node):
		print(node.val, end='')
	
	def Create(self, a, size, nodeId):
		if nodeId >= size or a[nodeId] == None:
			return None
		nowNode = self.GetTreeNode(nodeId)
		nowNode.val = a[nodeId]
		nowNode.left  = self.Create(a, size, nodeId*2)
		nowNode.right = self.Create(a, size, nodeId*2 + 1)
		return nowNode
	
	def CreateTree(self, a):
		self.root = self.Create(a, len(a), 1)
		
	def preOrder(self, node):
		if node:
			self.visit(node)
			self.preOrder(node.left)
			self.preOrder(node.right)

	def preOrderTraversal(self):
		self.preOrder(self.root)
		print('')
		
	def inOrder(self, node):
		if node:
			self.inOrder(node.left)
			self.visit(node)
			self.inOrder(node.right)

	def inOrderTraversal(self):
		self.inOrder(self.root)
		print('')
			
	def postOrder(self, node):
		if node:
			self.postOrder(node.left)
			self.postOrder(node.right)
			self.visit(node)
			
	def postOrderTraversal(self):
		self.postOrder(self.root)
		print('')

def Test():
	a = [ None, 'a', 'b', 'c', 'd', None, 'e', 'f', 'g', 'h', None, None, None, None, 'i' ]
	T = Tree(15)
	T.CreateTree(a)
	T.preOrderTraversal()
	T.inOrderTraversal()
	T.postOrderTraversal()

Test()