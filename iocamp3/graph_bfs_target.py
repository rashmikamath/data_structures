def bfs(graph, target):
	for node in graph.get_nodes():
		if node.get_state()=="UNVISITED" and bfs_visit(node, target):
			return True
	return False

def bfs_visit(node, target):
	q = Queue()
	q.enqueue(node)
	node.set_state("VISITING")
	while not Queue.isEmpty():
		node  = q.dequeue()
		if node.data == target:
			return True
		for nb in node.get_neighbor():
			if nb.get_state() == "UNVISITED":
				q.enqueue(nb)
				nb.set_state("VSITING")
		node.set_state("VISITED")

