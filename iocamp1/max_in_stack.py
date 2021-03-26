class MaxOfStack:
	def __init__(self):
		self.main = Stack()
		self.max_stack = Stack()

	def push_max(self, item):
		self.main.push(item)
		if self.max_stack.isEmpty() or item >= self.max_stack.peek():
			self.max_stack.push(item)

	def find_max(self):
		if self.max_stack.isEmpty():
			return 
		return self.max_stack.peek()

	def pop_max(self):
		if self.main.isEmpty():
			return
		item = self.main.pop()
		if self.max_stack.peek() == item:
			self.max_stack.pop()
		return item

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self, head=None):
		self.head = head

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

m_s = MaxOfStack()
m_s.push_max(1)
m_s.push_max(2)
m_s.push_max(7)
m_s.push_max(3)
m_s.push_max(10)
m_s.push_max(9)
val = m_s.find_max()
print(val)
