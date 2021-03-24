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

	def set_head(self, head):
		self.head = head

	def get_head(self):
		return self.head

	def set_tail(self, tail):
		self.tail = tail

	def get_tail(self):
		return self.tail

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

def sort_1_2_3(data):
	list1 = LinkedList()
	list2 = LinkedList()
	list3 = LinkedList()
	current = data.head
	print(current)
	while current is not None:
		if current == 0:
			list1.append(current)
		elif current == 1:
			list2.append(current)
		elif current == 2:
			list3.append(current)
		else:
			raise NotImplementedError("")
		current = current.get_next()
	if list1.tail is not None:
		list1.tail.next = None
	if list2.tail is not None:
		list2.tail.next = None
	if list3.tail is not None:
		list3.tail.next = None
	result = LinkedList()
	appendList(list1, result)
	appendList(list2, result)
	appendList(list3, result)
	return result

def appendList(toAppend, original):
	if toAppend is None or toAppend.head is None:
		return
	original.append(toAppend.head)
	original.tail = toAppend.tail
	return result

node1 = Node(1)
node2 = Node(0)
node3 = Node(2)
node4 = Node(1)
node5  = Node(2)
node6 = Node(1)
data_list = LinkedList()
data_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

sort_1_2_3(data_list).print_link_list()