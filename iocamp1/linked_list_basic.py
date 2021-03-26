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

	def print_link_list(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next

	def delete_node(self, toDelete, prev):
		if toDelete is None:
			return
		if toDelete == self.head:
			self.head = toDelete.next
		if toDelete == self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next

	def delete_node_noprev(self, toDelete):
		next = toDelete.get_next()
		if next == None:
			return 
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

def get_even_odd(input_list):
	odd = LinkedList()
	even = LinkedList()
	nodeIndex = 0
	current = input_list.get_head()
	while current != None:
		nodeIndex += 1
		if nodeIndex%2 == 0:
			destination = even
		else:
			destination = odd
		destination.append(current)
		current = current.get_next()
	if even.get_tail() is not None:
		even.get_tail().set_next(None)
	if odd.get_tail() is not None:
		odd.get_tail().set_next(None)
	even.print_link_list()
	odd.print_link_list()
	return even, odd

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
list_data.print_link_list()
list_data.delete_node(node1, None)
#list_data.delete_node_noprev(node3)
list_data.print_link_list()
#get_even_odd(list_data)