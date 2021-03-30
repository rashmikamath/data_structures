def bfs(graph, target):
	
	for node in graph.get_nodes():

		if node.get_state()=="UNVISITED" and bfs_visit(node, target):
			return True
	return False

def bfs_visit(node, target):
	import pdb
	pdb.set_trace()
	q = Queue(100)
	q.enqueue(node)
	node.set_state("VISITING")

	while not q.isEmpty():
		current = q.dequeue()

		if current.data== target:
			return True

		for nbr in current.get_neighbor():
			if nbr.get_state() == "UNVISITED":
				q.enqueue(nbr)
				nbr.set_state("VISITING")
		return False

class Queue:
	def __init__(self, capacity):
		self.capacity = capacity
		self.q = []
		self.front = 0
		self.rear = 0

	def isEmpty(self):
		if self.front == self.rear:
			return True
		else:
			return False

	def enqueue(self, node):
		if self.rear == self.capacity:
			print("Queue is full")
			return
		self.q.append(node)
		self.rear += 1

	def dequeue(self):
		if self.rear==self.front:
			print("Queue is empty")
			return
		del_ele = self.q.pop()
		self.rear -= 1
		return del_ele

	def print_queue(self):
		if self.rear == self.front:
			print("Queue is empty")
		for i in self.q:
			print(i.data)

	def size(self):
		if self.rear == self.front:
			print("Queue is full")
		count = 0
		for i in self.q:
			count += 1
		return count

class Graph:
	def __init__(self, nodes=[]):
		self.nodes = nodes

	def get_nodes(self):
		return self.nodes

	def add_node(self, node):
		return self.nodes.append(node)

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

print(bfs(g, 9))
