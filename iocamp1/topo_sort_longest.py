def diameter(start):
	
	if start==None:
		return 
	diameter = 0
	toposort = topo_sort(start)
	
	while not toposort.isEmpty():
		current = toposort.pop()
		print(diameter, current.get_longest_path())
		diameter = max(diameter, current.get_longest_path())
		for nb in current.get_neighbor():
			if current.get_longest_path()+1 > nb.get_longest_path():
				nb.set_longest_path(current.get_longest_path()+1)
	
	return diameter

def topo_sort(start):
	toposort = Stack()
	dfs_visit(start, toposort)
	return toposort

def dfs_visit(start, toposort):
	start.set_state("VISITING")
	for nb in start.get_neighbor():
		if nb.get_state()=="UNVISITED":
			dfs_visit(nb, toposort)
	start.set_state("VISITED")
	
	toposort.push(start)

class Stack:
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, item):
		if self.head== None:
			self.head = StackNode(item)
		else:
			new_node = StackNode(item)
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.isEmpty():
			return
		pop_node = self.head
		self.head = self.head.next
		pop_node.next = None
		return pop_node.data

	def peek(self):
		if self.isEmpty():
			return
		self.head.data.data

	def size(self):
		temp = self.head
		count = 0
		while temp is not None:
			print(temp.data.data)
			count += 1
			temp = temp.next
		return count

class StackNode:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def add_node(self, node):
		return self.nodes.append(node)

class GraphNode:
	def __init__(self, data, longest_path=0, state="UNVISITED", neighbors=[]):
		self.data = data
		self.state = state
		self.neighbors = neighbors
		self.longest_path = longest_path

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_state(self):
		return self.state

	def set_state(self, state):
		self.state = state

	def get_neighbor(self):
		return self.neighbors

	def add_neighbor(self, node):
		return self.neighbors.append(node)

	def get_longest_path(self):
		return self.longest_path

	def set_longest_path(self, value):
		self.longest_path = value

a = GraphNode("A")
b = GraphNode("B")
c = GraphNode("C")
d = GraphNode("D")
e = GraphNode("E")
f = GraphNode("F")
g = GraphNode("G")
h = GraphNode("H")
i = GraphNode("I")

gr = Graph()
gr.add_node(a)
gr.add_node(b)
gr.add_node(c)
gr.add_node(d)
gr.add_node(e)
gr.add_node(f)
gr.add_node(g)
gr.add_node(h)
gr.add_node(i)


a.add_neighbor(b)
a.add_neighbor(d)

b.add_neighbor(c)
b.add_neighbor(f)

d.add_neighbor(e)

f.add_neighbor(g)
f.add_neighbor(h)

e.add_neighbor(i)

h.add_neighbor(i)

print(diameter(a))