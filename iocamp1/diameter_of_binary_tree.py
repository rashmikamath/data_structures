def diameter(root):
	max_val = 1
	def helper(node):
		nonlocal max_val
		if node is None:
			return 0
		leftree = helper(node.left)
		righttree = helper(node.right)
		
		max_val = max(max_val, 1+leftree+righttree)
		return 1+max(leftree, righttree)
	helper(root)
	return max_val-1
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left=left
		self.right = right
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)
print(diameter(n1))