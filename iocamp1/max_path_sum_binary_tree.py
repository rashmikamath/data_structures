
def max_path_sum(root):
	max_val = float("-inf")
	def path_sum(node):
		nonlocal max_val
		if node is None:
			return 0
		leftpathsum = max(path_sum(node.left), 0)
		rightpathsum = max(path_sum(node.right), 0)
		current_path_sum = node.val+leftpathsum+rightpathsum
		max_val = max(max_val, current_path_sum)
		return node.val+max(leftpathsum, rightpathsum)
	path_sum(root)
	return max_val



class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)

print(max_path_sum(n1))