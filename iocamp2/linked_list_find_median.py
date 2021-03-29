def find_median(l):
	# if l.head == None or l.tail == None:
	# 	return
	fast = l.head
	slow = l.head
	while fast.get_next() is not None:
		fast = fast.get_next()
		if fast.get_next() is not None:
			fast = fast.get_next()
			slow = slow.get_next()
	return slow.data

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def set_head(self,head):
		self.head = head

	def get_head(self):
		return self.head

	def set_tail(self, tail):
		self.tail = tail 

	def get_tail(self):
		return self.tail 

	def append(self, append_node):
		if self.head == None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def delete_node(self, toDelete, prev):
		if toDelete is None:
			return
		if toDelete==self.head:
			self.head = toDelete.get_next()
		if toDelete==self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next 

	def delete_without_prev(self, toDelete):
		next = toDelete.next()
		if next is None:
			return 
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
list_data = LinkedList()
list_data.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7


print(find_median(list_data))