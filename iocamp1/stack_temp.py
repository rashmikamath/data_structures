class Node:
	def __init__(self, data,next=None):
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
		temp = Node(item)
		if self.head is None:
			self.head = temp
		else:
			new_node = temp
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

s = Stack()
s.push(1)
s.push(2)
s.push(4)
s.push(6)
s.push(3)
s.print_stack()
def find_target(s, val):
	temp = Stack()
	while not s.isEmpty():	 
		if s.peek()==val:
			print("Found")
			break
		temp.push(s.pop())

	while not temp.isEmpty():
		s.push(temp.pop())

find_target(s, 6)
