class Queue:
	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, item):
		self.s1.push(item)

	def dequeue(self):
		if self.s2.isEmpty():
			self.flushtos2()

		if self.s2.isEmpty():
			print("Invalid")
		return self.s2.pop()

	def flushtos2(self):
		while not self.s1.isEmpty():
			self.s2.push(self.s1.pop())

	def print_queue(self):
		self.s1.print_size()

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Stack:
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head ==None:
			return True
		else:
			return False

	def push(self, item):
		if self.head==None:
			self.head = Node(item)
		else:
			new_node = Node(item)
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.isEmpty():
			return
		pop_node = self.head
		self.head  = self.head.next
		pop_node.next = None
		return pop_node.data

	def print_size(self):
		temp = self.head
		count = 0
		while temp is not None:
			print(temp.data)
			count += 1
			temp = temp.next
		return count

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()
val = q.dequeue()
print(val)