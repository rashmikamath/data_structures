def topo_sort(root):
	s = Stack()
	dfs_visit(root, s)
	return s

def dfs_visit(root, s):
	root.set_state("VISITING")
	for nb in root.get_neighbor():
		if nb.get_state() == "UNVISITED":
			dfs_visit(nb, s)
	root.set_state("VISITED")
	s.push(root)


def diameter(root):
	toposort = topo_sort(root)
	diameter = 0
	while not toposort.isEmpty():
		current = toposort.pop()
		diameter = max(diameter, current.path)
		for nb in current.get_neighbor():
			if current.path+1> nb.path:
				nb.set_path(current.path+1)
	return diameter