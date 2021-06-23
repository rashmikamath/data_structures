def isBalanced(root):
	if root==None:
		return 0
	rightH = isBalanced(root.right)
	leftH = isBalanced(root.left)
	if rightH==-1 and leftH==-1:
		return -1
	if abs(rightH)-abs(leftH) > 1:
		return -1
	return 1+max(rightH, leftH)

def is