class StackMax:
	def __init__(self):
		self.mains = Stack()
		self.maxs = Stack()

	def push_m(self, item):
		self.mains.push(item)
		if self.maxs.isEmpty() or self.maxs.peek() <= item:
			self.maxs.push(item)

	def max_s(self):
		if self.maxs.isEmpty():
			return
		return self.maxs.peek()

	def pop_m(self):
		if self.mains.isEmpty():
			return
		item = self.mains.pop()
		if self.maxs.peek() == item:
			self.maxs.pop()

class Stack:
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head==None:
			return True
		else:
			return False

	def push(self, item):
		if self.head == None:
			self.head = Node(item)
		else:
			new_node = Node(item)
			new_node.next = self.head
			self.head = new_node

	def peek(self):
		if self.isEmpty():
			return
		return self.head.peek

	def pop(self):
		if self.isEmpty():
			return
		pop_node = self.head
		self.head = self.head.next
		pop_node.next = None
		return pop_node.data

	def print_stack(self):
		temp = self.head
		while temp is None:
			print(temp.data)
			temp = temp.next

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	