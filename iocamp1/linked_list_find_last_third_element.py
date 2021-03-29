def last_third_element(l):
	pointer1 = l.head
	pointer2 = l.head.next.next
	while pointer2.get_next() is not None:
		pointer2 = pointer2.get_next()
		pointer1 = pointer1.get_next()
	return pointer1.data

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def get_head(self):
		return self.head

	def set_head(self, head):
		self.head = head 

	def get_tail(self):
		return self

	def set_tail(self, tail):
		self.tail = tail 

	def append(self, append_node):
		if self.head == None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def delete_node(self, toDelete, prev):
		if toDelete is None:
			return

		if toDelete == self.head:
			self.head = toDelete.get_next()
		if toDelete == self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next 

	def delete_without_prev(self, toDelete):
		next = toDelete.get_next()
		if next is None:
			return
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node5 = Node(500)
node6 = Node(600)
node7 = Node(700)
list_data = LinkedList()
list_data.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = None
print(last_third_element(list_data))