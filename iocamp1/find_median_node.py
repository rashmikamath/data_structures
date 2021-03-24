class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

class LinkedList():
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def get_head(self):
		return self.head

	def set_head(self, head):
		self.head = head

	def get_tail(self):
		return self.tail

	def set_tail(self, tail):
		self.tail = tail

	def append(self, append_value):
		if self.head is None:
			self.head = append_value
		else:
			self.tail = self.tail.set_next(append_value)
		self.tail = append_value

	def delete_node(self, toDelete, prev):
		if toDelete is None:
			return
		if toDelete == self.head:
			self.head = toDelete.get_next()
		if toDelete == self.tail:
			self.tail = prev
		if toDelete is not None:
			prev.next = toDelete.next

	def delete_node_without_prev(self, toDelete):
		next = toDelete.get_next()
		if next is None:
			return 
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

def get_median(head):
	fast = head
	slow = head
	while fast.get_next() is not None:
		fast = fast.get_next()
		if fast.get_next() is not None:
			fast = fast.get_next()
			slow = slow.get_next()
	return slow

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
data_list = LinkedList()
data_list.head = node1
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
print(get_median(node1).get_data())