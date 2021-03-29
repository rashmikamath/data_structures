def bfs_print_level(root):
	current_level = Queue(100)
	next_level = Queue(100)
	current_level.add(root)
	root.set_state("VISITING")
	while not current_level.isEmpty():
		curr = current_level.pop()
		print(curr.data)
		for neighbor in curr.get_neighbor():
			if neighbor.get_state() == "UNVISITED":
				next_level.add(neighbor)
				neighbor.set_state("VISITING")
		curr.set_state("VISITED")
		if current_level.isEmpty():
			
			current_level=next_level
			next_level=Queue(100)

class Queue:
	def __init__(self, capacity):
		self.q = []
		self.front = 0
		self.rear = 0
		self.capacity = capacity

	def add(self, item):
		if self.rear == self.capacity:
			print("Queue is full")
		self.q.append(item)
		self.rear += 1

	def pop(self):
		if self.rear == self.front:
			print("Queue is empty")
		last = self.q.pop(0)
		self.rear -= 1
		return last

	def isEmpty(self):
		return self.rear == self.front

	def size(self):
		if self.rear == self.front:
			ptint("Queue is empty")
		count = 0
		for i in range(len(self.q)):
			count += 1
		return count

	def print_queue(self):
		if self.rear == self.front:
			ptint("Queue is empty")
		for i in range(len(self.q)):
			print(self.q[i].data)

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def add_node(self, node):
		return self.nodes.append(node)

	def get_nodes(self):
		return self.nodes 

class Node:
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

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
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
print(bfs_print_level(n1))
