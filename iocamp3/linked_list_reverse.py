def reverse(l):
	curr = l.head
	prev = Node(data=None)
	while curr is not None:
		next = curr.next
		curr.set_next(prev)
		prev = curr
		curr = next
	return prev

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def append(self, append_node):
		if self.head == None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def delete_node(self, toDelete, prev):
		if toDelete==None:
			return
		if toDelete==self.head:
			self.head = toDelete.next 
		if toDelete==self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next

	def delete_no_prev(self, toDelete):
		next = toDelete.next
		if next==None:
			return
		toDelete.set_data(next.get_data())
		self.delete_no_prev(next, toDelete)

	def print_ll(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next


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
		self.next = node 

def append_linklist(toappend, original):
	if toappend == None or original == None:
		return 
	original.append(toappend.head)
	original.tail = toappend.tail



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)



l = LinkedList()
l.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9

r = reverse(l)
r.print_ll()