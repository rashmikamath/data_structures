def bfs_visit(root):
	currentlevel = Queue()
	nextlevet = Queue()
	currentlevel.enqueue(root)
	root.set_state("VISITING")
	while not currentlevel.isEmpty():
		current = currentlevel.dequeue()
		print(current.data)
		for nb in current.get_neighbor():
			if nb.get_state() == "UNVISITED":
				nextlevet.enqueue(nb)
				nb.set_state("VISITING")
	if currentlevel.isEmpty():
		currentlevel = nextlevet
		nextlevet = Queue()
