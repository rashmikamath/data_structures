def path_func(root):
	path = Stack()
	printpath(root, path)

def printpath(root, path):
	if root==None:
		return root
	path.push(root)
	if root.left==None and root.right==None:
		print(path)
	printpath(root.left, path)
	printpath(root.right, path)
	path.pop()