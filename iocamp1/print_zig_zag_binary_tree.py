def print_zig_zag(root):
	
	stack = [root]
	temp = []
	res = []
	flag = 1
	while stack != []:
		for i in range(len(stack)):
			curr  = stack.pop(0)
			temp.append(curr.data)
			if curr.left:
				stack.append(curr.left)
			if curr.right:
				stack.append(curr.right)
		res += [temp[::flag]]
		temp = []
		flag *= -1
	return res

class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n2 = Node(2, n4, n5)
n3 = Node(3, n6, n7)
n1 = Node(1, n2, n3)



print(print_zig_zag(n1))