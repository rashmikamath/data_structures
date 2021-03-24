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

	def delete_without_prev(self, toDelete):
		next = toDelete.get_next()
		if next is None:
			return
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

	def get_median(self):
		slow = self.head
		fast = self.head
		while fast.get_next() is not None:
			fast = fast.get_next()
			if fast.get_next() is None:
				break
			fast = fast.get_next()
			slow = slow.get_next()
		return slow 

	def reverse_link_list(self, head):
		prev = None
		curr = self.head
		while curr is not None:
			next = curr.get_next()
			curr.set_next(prev)
			prev = curr
			curr = next 
		return prev

	def isPalindrome(self):
		median = self.get_median()
		last = self.reverse_link_list(median)
		start = self.head
		end  = last
		while start is not None and end is not None:
			if start.get_data() != end.get_data():
				return False
			start = start.get_next()
			end = end.get_next()
		return True

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("B")
node5 = Node("C")

list_data = LinkedList()
list_data.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(list_data.isPalindrome())