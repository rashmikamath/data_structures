class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack():
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			new_node = Node(data)
			new_node.next = self.head
			self.head = new_node

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

def find_value(target, s):
	temp = Stack()
	target_found = False
	while not s.isEmpty():
		if s.peek() == target:
			target_found = True
			break
		temp.push(s.pop())
	while not temp.isEmpty():
		s.push(temp.pop())
	return target_found

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.print_stack()
print(find_value(6, s))

