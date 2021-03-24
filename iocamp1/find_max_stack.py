class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack():
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head is None:
			return True
		else:
			return False


	def push(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head  = new_node

	def pop(self):
		if self.isEmpty():
			return None
		else:
			pop_node = self.head
			self.head = self.head.next
			pop_node.next = None
			return pop_node.data

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.head.data

	def print_stack(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next


class MaxStack():
	main = Stack()
	max_stack = Stack()

	def push_max(self, a):
		main.push(a)
		if max_stack.isEmpty() or a>=main.peek():
			max_stack.push(a)

	def max_val(sefl):
		if max_stack.isEmpty():
			raise NotImplementedError("Max stack is empty")
		return max_stack.peek()

	def pop(self):
		if main.isEmpty():
			raise NotImplementedError("Main stack is empty")
		item = main.pop()
		if max_stack.peek() == item:
			max_stack.pop()
		return item

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(8)
s.push(5)
s.print_stack()
m_stack = MaxStack()
m_stack.