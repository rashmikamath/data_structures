class StackAsQueue:
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def flushtos2(self):
		while not self.s1.isEmpty():
			self.s2.push(self.s1.pop())

	def enqueue(self, a):
		self.s1.push(a)


	def dequeue(self):
		if self.s2.isEmpty():
			self.flushtos2()
		if self.s2.isEmpty():
			raise("s2 is empty")
		return self.s2.pop()


class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self, head=None):
		self.head =head

	def isEmpty(self):
		if self.head == None:
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
		return self.head.data

	def print_stack(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next

q = StackAsQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()

