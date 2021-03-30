def topo_sort(node):
	s = Stack()
	
	dfs_visit(node, s)
	
	return s

def dfs_visit(node, stack):
	node.set_state("VISITING")
	for nb in node.get_neighbor():
		
		if nb.get_state() == "UNVISITED":
			dfs_visit(nb, stack)
	node.set_state("VISITED")
	stack.push(node)

class Stack_Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next= next

	def get_data(self):
		return self.data 

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

	def set_data(self, data):
		self.data = data

class Stack:
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False

	def push(self, item):
		if self.head is None:
			self.head = Stack_Node(item)
		else:
			new_node = Stack_Node(item)
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.isEmpty(self):
			return
		pop_node = self.head
		self.head = self.head.next 
		pop_node.next = None 
		return pop_node.data

	def peek(self):
		if self.isEmpty():
			return
		return self.head.data 

	def size(self):
		temp = self.head
		count = 0
		while temp is not None:
			print(temp.data.data)
			count += 1
			temp = temp.next
		return count

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def add_node(self, node):
		return self.nodes.append(node)

class GraphNode:
	def __init__(self, data, state="UNVISITED", neighbor=[]):
		self.data = data
		self.state = state 
		self.neighbor = neighbor

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_state(self):
		return self.state 

	def set_state(self, state):
		self.state = state 

	def get_neighbor(self):
		return self.neighbor

	def add_neighbor(self, node):
		return self.neighbor.append(node)

n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)
n4 = GraphNode(4)
n5 = GraphNode(5)
n6 = GraphNode(9)
g = Graph()
g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
#g.add_node(n6)

n1.add_neighbor(n2)
n1.add_neighbor(n4)

n2.add_neighbor(n4)
n2.add_neighbor(n3)
n2.add_neighbor(n5)

n3.add_neighbor(n5)


s1 = topo_sort(n1)
s1.size()
