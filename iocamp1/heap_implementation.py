class MaxHeap:
	def __init__(self, capacity):
		self.capacity = capacity
		self.a = []
		self.size = 0

	def parent_func(self, i):
		return (i-1)/2

	def left(self, i):
		return (2*i+1)

	def right(self, i):
		return (2*i+2)

	def isValid(self, i):
		return i>=0 and i<=size
		

	def propagate(self, i):
		parent = self.parent_func(i)

		while i>0 and self.a[parent] < self.a[i]:
			swap(self.a, parent, i)
			i = parent
			parent = self.parent_func(i)

	def insert(self, item):
		if self.size == 0:
			return

		item_index = self.size

		self.a[self.size] = item 
		self.size += 1
		self.propagate(item_index)

	def remove_max(self):
		if self.size == 0:
			return
		swap(self.a, 0, size-1)
		self.heapify(i)

	def remove_node(self, i):
		if not self.isValid(i):
			return
		swap(self.a, i, size-1)
		size -= 1
		if i!=0 and self.a[parent_func(i)] < self.a[i]:
			self.propagate(i)
		else:
			self.heapify(i)

	def heapify(self, i):
		if not self.isvalid(i):
			return 

		if self.isvalid(self.left(i)):
			left_val = self.a[self.left(i)]
		else:
			left_val = float('-inf')
		return left_val

		if self.isvalid(self.right(i)):
			right_val = self.a[self.right(i)]
		else:
			right_val = float("-inf")
		return right_val

		max_val = max(max(right_val, left_val), self.a[i])

		max_index = i
		if max_val = right_val:
			max_index = self.right(i)
		elif max_val = left_val:
			max_index = self.left(i)

		if max_index!=i:
			swap(self.a, max_index, i)
			self.heapify(max_index)