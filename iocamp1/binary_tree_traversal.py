class TreeNode:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_left(self):
		return self.left

	def set_left(self, left):
		self.left = left 

	def get_right(self):
		return self.right

	def set_right(self, right):
		self.right = right

def InorderTraversal(node):
	if node==None:
		return
	InorderTraversal(node.get_left())
	print(node.data)
	InorderTraversal(node.get_right())


def PreOrderTraversal(node):
	if node == None:
		return
	print(node.data)
	PreOrderTraversal(node.get_left())
	PreOrderTraversal(node.get_right())

def PostOrderTraversal(node):
	if node==None:
		return
	PostOrderTraversal(node.get_left())
	PostOrderTraversal(node.get_right())
	print(node.data)

n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, n6, n7)
n1 = TreeNode(1, n2, n3)
InorderTraversal(n1)
print("InorderTraversal")
PreOrderTraversal(n1)
print("PreorderTraversal")

PostOrderTraversal(n1)
print("PostOrderTraversal")
