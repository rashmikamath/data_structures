def height(root):
	res = -1

	height(root, -1, res)
	return res


def height(root, prevdepth, maxdepth):
	if root==None:
		return
	currdepth = prevdepth + 1
	if currdepth > maxdepth:
		maxdepth = currdepth
	height(root.left, currdepth, maxdepth)
	height(root.right, currdepth, maxdepth)

	return maxdepth