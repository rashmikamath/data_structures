class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def add_node(self, node):
		self.nodes.append(node)

class Node:
	def __init__(self, data, state="UNVISITED", neighbors=[]):
		self.data = data
		self.state = state
		self.neighbors = neighbors

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state 

	def get_neigbhors(self):
		return self.neighbors

	def add_neighbor(self, neighbor):
		self.neighbors.append(neighbor)

def dfs(graph, target):
	for node in graph.get_nodes():
		if node.get_state() == "UNVISITED" and dfs_visit(node, target):
			return True
	return False

def dfs_visit(node, target):
	node.set_state("VISITING")
	if node.data == target:
		return True
	for nb in node.get_neigbhors():
		if nb.get_state() == "UNVISITED" and dfs_visit(nb, target):
			return True
			

	node.set_state("VISITED")
	return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(9)
g = Graph()
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
g.add_node(n6)

n1.add_neighbor(n2)
n1.add_neighbor(n3)

n2.add_neighbor(n4)

n3.add_neighbor(n4)
n3.add_neighbor(n5)

n4.add_neighbor(n6)

n5.add_neighbor(n6)

print(dfs(g, 9))