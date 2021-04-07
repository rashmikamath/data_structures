class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.map_dict = dict()
		self.head = Node()

	def read(self, key):
		node = map_dict.get(key)
		if node==None:
			return
		remove(key)
		add(key, value)
		

	def write(self, key, value):
		if self.capacity==len(map_dict):
			remove(self.head.data)
		add(key, value)

	def add(self, key, value):
		node = value
		append_ll(node)
		map_dict[key] = node

	def remove(self, key):
		if key not in map_dict.keys():
			return
		node = map_dict.get(key)
		remove_ll(node)
		map_dict.pop(key)

	def append_ll(self, append_node):
		if self.head == None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def remove_ll(self, toDelete):
		next = toDelete.next
		if next==None:
			return 
		toDelete.set_data(next.get_data)
		self.delete_node_prev(next, toDelete)

	def remove_ll_prev(self, toDelete, prev):
		if toDelete==None:
			return
		if toDelete==self.head:
			self.head = toDelete.next 
		if toDelete == self.tail:
			self.tail = prev
		if prev is not None:
			prev.next = toDelete.next

