class Node:
	def __init__(self, key, value, next=None):
		self.key = key
		self.value = value
		self.next = next

	def get_key(self):
		return self.key

	def set_key(self, data):
		self.key = data

	def get_value(self):
		return self.value

	def set_next(self, next):
		self.next = next

	def get_next(self):
		return self.next

class LRU:
	def __init__(self, capacity):
		self.capacity = capacity
		self.map_dict = dict()
		self.head = Node(0, 0)
		self.tail = Node(0, 0)

	def read(self, key):
		node = self.map_dict[key]
		if node==None:
			return
		self.remove(key)
		self.add(node.get_key(), node.get_value())
		return node.get_value()

	def write(self, key, value):
		if len(self.map_dict) == self.capacity:
			self.remove(self.head.get_key())
		self.add(key, value)

	def remove(self, key):
		if key not in self.map_dict.keys():
			return 
		toRemove = self.map_dict[key]
		self.deletell(toRemove)
		self.map_dict.pop(key)

	def add(self, key, value):
		new_node = Node(key, value)
		self.appendll(new_node)
		self.map_dict[key] = new_node

	def appendll(self, append_node):
		if self.head==None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def deletell(self, toDelete):
		next = toDelete.get_next()
		if next is None:
			return 
		toDelete.set_key(next.get_key())
		self.deletellprev(next, toDelete)

	def deletellprev(self, toDelete, prev):
		if toDelete == None:
			return
		if toDelete==self.head:
			self.head = toDelete.next
		if toDelete==self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next

lru = LRU(5)
n1 = Node(1, 1)
n2 = Node(2, 2)
n3 = Node(3, 3)
n4 = Node(4, 4)
n5 = Node(5, 5)
lru.write(1,1)
lru.write(2,2)
lru.write(3,3)
lru.write(4,4)
lru.write(5,5)
lru.write(6,6)

print(lru.read())


