def dfs(graph, target):
	# import pdb
	# pdb.set_trace()
	for node in graph.get_node():
		if node.get_state() == "UNVISITED" and dfs_visit(node, target):
			return True
	return False


def dfs_visit(node, target):

	node.set_state("VISITNG")

	if node.get_data() == target:
		return True
	for neighbor in node.get_neighbor():
		if neighbor.get_state() == "UNVISITED" and dfs_visit(neighbor, target):
			return True
	node.set_state("VISITED")
	return False

class Node:
	def __init__(self, data, state="UNVISITED", neighbor=[]):
		self.data = data
		self.state = state
		self.neighbor = neighbor

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def add_neighbor(self, node):
		self.neighbor.append(node)

	def get_neighbor(self):
		return self.neighbor

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def add_node(self, data):
		self.nodes.append(data)

	def get_node(self):
		return self.nodes

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

