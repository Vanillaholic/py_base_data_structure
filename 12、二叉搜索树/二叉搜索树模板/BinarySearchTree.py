class TreeNode:
	def __init__(self, val=None, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self):
		self.root = None
		
	def insertNode(self, node, value):
		if node == None:
			return TreeNode(value)
		if value < node.val:
			node.left = self.insertNode(node.left, value)
		elif value > node.val:
			node.right = self.insertNode(node.right, value)
		return node
	
	def insert(self, value):
		self.root = self.insertNode(self.root, value)
	
	def removeNode(self, node, value):
		if node == None:
			return None

		if value < node.val:
			node.left = self.removeNode(node.left, value)
		elif value > node.val:
			node.right = self.removeNode(node.right, value)
		else:
			if node.left == None and node.right == None:
				return None
			elif node.left == None:
				return node.right
			elif node.right == None:
				return node.left
			else:
				replacement = node.right
				while replacement.left:
					replacement = replacement.left
				node.val = replacement.val
				node.right = self.removeNode(node.right, replacement.val)
		return node
	
	def remove(self, value):
		self.root = self.removeNode(self.root, value)
    
	def searchNode(self, node, value):
		if node == None:
			return False
		if value < node.val:
			return self.searchNode(node.left, value)
		elif value > node.val:
			return self.searchNode(node.right, value)
		return True
	
	def search(self, value):
		return self.searchNode(self.root, value)

	def inOrder(self, node):
		if node:
			self.inOrder(node.left)
			print(node.val, end=',')
			self.inOrder(node.right)
	
	def inOrderTraversal(self):
		self.inOrder(self.root)
		print('')

def Test():
    bst = BinarySearchTree()

    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(40)
    bst.insert(80)
    bst.insert(60)
    bst.insert(100)
	
    bst.inOrderTraversal()
    print("≤È’“ 100£∫", bst.search(100))
    print("≤È’“ 90£∫", bst.search(90))

    bst.remove(70)
    bst.inOrderTraversal()
    
    bst.insert(65)
    bst.inOrderTraversal()


Test()