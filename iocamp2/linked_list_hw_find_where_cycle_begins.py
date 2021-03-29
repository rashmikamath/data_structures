def where_cycle_begins(l):
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
	counter = 1
	while fast != slow:
		fast = fast.get_next()
		counter += 1
	slow = slow.get_next()

	front = l.head
	back = l.head
	for i in range(counter):
		front = front.get_next()
	while front != back:
		front = front.get_next()
		back = back.get_next()
	return back.data

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
			self.head = toDelete.next
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

print(where_cycle_begins(list_data))
