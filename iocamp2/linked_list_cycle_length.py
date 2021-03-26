def lenght_of_linked_list_cycle(l):
	fast = l.head
	slow = l.head
	while fast is not None:
		fast = fast.get_next()
		if fast == slow:
			break
		if fast is not None:
			fast = fast.get_next()
			if fast == slow:
				break
		slow = slow.get_next()

	if fast==None:
		return -1

	
	fast = fast.get_next()
	node_passed = 1
	if fast!=slow:
		fast = fast.get_next()
		node_passed += 1
	return node_passed

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

	def set_head(self, head):
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
		if toDelete == self.head:
			self.head  = toDelete.next 
		if toDelete == self.tail:
			self.tail = prev 
		if prev is not None:
			prev.next = toDelete.next 

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
print(lenght_of_linked_list_cycle(list_data))