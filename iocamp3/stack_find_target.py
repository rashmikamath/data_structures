def find_target(s, target):
	temp = Stack()
	found = False
	while not s.isEmpty():
		top = s.peek()
		if top==target:
			found=True
			break
		
		temp.push(s.pop())
	while not temp.isEmpty():
		s.push(temp.pop())
	return found

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

	def pop(self):
		if self.isEmpty():
			print("Stack is empty")
			return 
		pop_node = self.head
		self.head = self.head.next
		pop_node.next = None
		return pop_node

	def peek(self):
		if self.isEmpty():
			print("Stack is empty")
		return self.head.data

	def print_stack_size(self):
		temp = self.head
		count = 0
		while temp is not None:
			print(temp.data)
			count+=1
			temp = temp.next
		return count

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next



s = Stack()
s.push(5)
s.push(4)
s.push(3)
s.push(2)
s.push(1)
s.print_stack_size()
print(find_target(s, 5))