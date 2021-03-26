def hascycle(l):
	slow = l.head
	fast = l.head
	while fast is not None:
		fast = fast.get_next()
		if fast==slow:
			return True
		if fast is not None:
			fast = fast.get_next()
			if fast==slow:
				return True
		slow = slow.get_next()
	return False

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def set_data(self, item):
		self.data = item

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
		return self.tail

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
		if self.head == toDelete:
			self.head = toDelete.get_next() 
		if self.tail == toDelete:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next

	def delete_without_prev(self, toDelete):
		next = toDelete.get_next()
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
node6.next = node3

print(hascycle(list_data))

