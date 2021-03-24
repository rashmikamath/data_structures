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

	def print_linked_list(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next

def check_has_cycle(head):
	fast = head
	slow = head
	while fast is not None:
		fast = fast.get_next()
		if fast == slow:
			return True
		if fast is not None:
			fast = fast.get_next()
			if fast == slow:
				return True
		slow = slow.get_next()
	return False

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
print(check_has_cycle(node1))	
