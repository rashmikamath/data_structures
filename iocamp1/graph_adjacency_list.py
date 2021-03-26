class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [None]*self.vertices

	def add_edge(self, src, dst):
		new_node = Node(dst)
		new_node.next = self.graph[src]
		self.graph[src] = new_node

		new_node = Node(src)
		new_node.next = self.graph[dst]
		self.graph[dst] = new_node

	def print_graph(self):
		for i in range(self.vertices):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp is not None:
				print(" -> {}".format(temp.data), end="")
				temp = temp.next

graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.print_graph()