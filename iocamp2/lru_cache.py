class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.head = None
		self.tail = None
		self.d = dict()

	def read(self, key):
		node = self.d.get(key)
		if node==None:
			return
		self.remove(key)
		self.add(key, node)
		return node.get_data()

	def write(self, key, val):
		if len(self.d) == self.capacity:
			self.remove(self.head.data)
		self.add(key, val)

	def remove(self, key):
		if key not in self.d.keys():
			return
		toRemove = self.d.get(key)
		self.delete_ll(toRemove)
		self.d.pop(key)

	def add(self, key, val):
		new_node = val
		self.append_ll(new_node)
		self.d.setdefault(key, val)

	def append_ll(self, append_node):
		if self.head==None:
			self.head=append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def delete_ll(self, toDelete):
		next = toDelete.next
		if next is None:
			return 
		toDelete.set_data(next.get_data)
		self.delete_with_prev(next, toDelete)

	def delete_with_prev(self, toDelete, prev):
		if toDelete is None:
			return

		if toDelete==self.head:
			self.head = toDelete.next 
		if toDelete==self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next 

	def print_ll(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next


class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next 

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next

	def get_data(self):
		return self.data

	def set_data(self, data):
		self.data = data

lru = LRUCache(5)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
lru.write(n1.data, n1)
print(lru.read(n1.data))
print("==================n1")
lru.write(n2.data, n2)
lru.write(n3.data, n3)
lru.write(n4.data, n4)
print(lru.read(n4.data))
print("===========n4")
lru.write(n5.data, n5)
print("======before_maxout=====")
lru.print_ll()

lru.write(n6.data, n6)
print("======after_maxout=====")
import pdb
pdb.set_trace()
lru.print_ll()
