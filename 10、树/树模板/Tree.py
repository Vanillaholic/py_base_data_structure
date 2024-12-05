class TreeNode:
    def __init__(self):
        self.data = None
        self.childrenList = []

    def AddChild(self, tNode):
        self.childrenList.append( tNode )
		

class Tree:
	def __init__(self, maxNodes):
		self.root = None
		self.nodes = [TreeNode() for i in range(maxNodes)]
	
	def GetTreeNode(self, id):
		return self.nodes[id]
	
	def SetRoot(self, rootId):
		self.root = self.GetTreeNode(rootId)
	
	def AddChild(self, parentId, sonId):
		pNode = self.GetTreeNode(parentId)
		sNode = self.GetTreeNode(sonId)
		pNode.AddChild(sNode)
	
	def AssignData(self, nodeId, data):
		self.GetTreeNode(nodeId).data = data
	
	def Print(self, node = None):
		if node == None:
			node = self.root
		print(node.data, end='')
		for child in node.childrenList:
			self.Print(child)

def Test():
    T = Tree(9)
    T.SetRoot(0)
    T.AssignData(0, 'a')
    T.AssignData(1, 'b')
    T.AssignData(2, 'c')
    T.AssignData(3, 'd')
    T.AssignData(4, 'e')
    T.AssignData(5, 'f')
    T.AssignData(6, 'g')
    T.AssignData(7, 'h')
    T.AssignData(8, 'i')

    T.AddChild(0, 1)
    T.AddChild(0, 2)
    T.AddChild(1, 3)
    T.AddChild(2, 4)
    T.AddChild(2, 5)
    T.AddChild(3, 6)
    T.AddChild(3, 7)
    T.AddChild(3, 8)

    T.Print()
	
Test()