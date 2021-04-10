class TreeNode:
	def __init__(self, data, visited=False, left=None, right=None):
		self.data = data
		self.visited = visited
		self.left = left
		self.right = right

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_right(self):
		return self.right

	def set_right(self, right):
		self.right = right

	def get_left(self):
		return self.left

	def set_left(self, left):
		self.left = left

	def set_visit(self, visit):
		self.visited = visit

	def isvisted(self):
		return self.visited

class Stack:
	def __init__(self, capacity):
		self.capacity=capacity
		self.a = []
		self.size = 0

	def push(self, item):
		if self.capacity == self.size:
			return
		self.a.append(item)
		self.size += 1

	def pop(self):
		if self.size==0:
			return
		self.a.pop()
		self.size -= 1

	def peek(self):
		if self.size == 0:
			return

		return self.a[self.size]

	def isEmpty(self):
		if self.size==0:
			return True
		else:
			return False

	def print_stack(self):
		if self.size == 0:
			return
		for i in len(self.size):
			print(self.a[i])


def inorder_iterative(root):
	if root == None:
		return
	s = Stack(100)
	s.push(root)
	InorderTraversal(root, s)

def InorderTraversal(node, s):
	

	s.push(node)

	while not s.isEmpty():
		node = s.pop()
		
		if node.isvisted():
			print(node.data)
		else:
			node.set_visit(True)
			if node.get_left!=None:
				s.push(node.left)
			s.push(node)
			if node.get_right!=None:
				s.push(node.left)
		s.print_stack()

n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, n6, n7)
n1 = TreeNode(1, n2, n3)

print(inorder_iterative(n1))