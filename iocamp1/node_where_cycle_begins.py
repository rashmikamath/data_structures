class Node:
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
		self.node = node

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

	def print_link_list(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.get_next()

def node_begin_cycle(head):
	slow = head
	fast = head
	while fast is not None:
		fast = fast.get_next()
		if fast == slow:
			break
		if fast is not None:
			fast = fast.get_next()
			if fast == slow:
				break
		slow = slow.get_next()
	if fast == None:
		return
	index = 1
	fast = fast.get_next()
	while fast != slow:
		fast = fast.get_next()
		index += 1
	front = head 
	back = head
	for i in range(index):
		front = front.get_next()
	while front!=back:
		front = front.get_next()
		back = back.get_next()
	return front

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
node6.next = node1
print(node_begin_cycle(node1).get_data())
