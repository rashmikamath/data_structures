def clone_graph(root):
	if root == None:
		return 
	map_dict = dict()
	root_copy = Node(root.get_data())
	map_dict[root] = root_copy
	dfs_visit(root, map_dict)
	return root_copy

def dfs_visit(root, map_dict):
	root.set_state("VISITING")
	for neighbor in root.get_neighbor():
		if neighbor not in map_dict.keys():
			map_dict[neighbor] = Node(neighbor.get_data())
			root_copy = map_dict.get(root)
			neighbor_copy = map_dict.get(neighbor)
			if neighbor.get_state() == "UNVISITED":
				dfs_visit(neighbor, map_dict)
	root.set_state("VISITED")

class Node:
	def __init__(self, data, state="UNVISITED", neighbor=[]):
		self.data = data
		self.state = state
		self.neighbor = neighbor

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def get_neighbor(self):
		return self.neighbor

	def add_neighbor(self, item):
		self.neighbor.append(item)

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def add_node(self, node):
		self.nodes.append(node)

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

n1_copy = clone_graph(n1)

for n in n1_copy.get_neighbor():
	print(n.get_data())



