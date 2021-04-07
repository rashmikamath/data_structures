class MaxHeap:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.a = []

	def parent_f(self,i):
		return (i-1)//2

	def left(self,i):
		return 2*i+1

	def right(self,i):
		return 2*i+2

	def isvalid(self,i):
		return i >=0 and i<=self.size

	def swap(self, i, j):
		temp = self.a[i]
		self.a[i] = self.a[j]
		self.a[j] = temp

	def propagate(self,i):
		if not self.isvalid(i):
			return
		parent = parent_f(i)
		if self.a[parent] < self.a[i]:
			self.swap(i, parent)
			i = parent
			parent = parent_f(i)

	def heapify(self, i):
		if not self.isvalid(i):
			return 
		if self.isvalid(self.left(i)):
			left_val = self.a[self.left(i)]
		else:
			left_val = float("-inf")

		if self.isvalid(self.right(i)):
			right_val = self.a[self.right(i)]
		else:
			right_val = float("-inf")
		max_val = max(max(right_val, left_val), self.a[i])

		max_index = i
		if max_val==right_val:
			max_index = self.right(i)
		else:
			max_index = self.left(i)

		if max_index!=i:
			self.swap(i, max_index)
			self.heapify(max_index)

	def insert(self, item):
		if self.size == self.capacity:
			print("Heap is full")
		item_index = self.size
		self.a[self.size] = item
		self.size += 1
		self.propagate(item_index)

	def remove(self):
		if self.size==0:
			return
		self.swap(0, size-1)
		self.heapify(0)

	def peek(self):
		if self.size == 0:
			return 
		return self.a[0]

def find_k_smallest_element(arr, k):
	h = MaxHeap(k)
	if len(arr)==0 or k==None or arr=None:
		return
	for i in range(len(arr)):
		if i<k:
			h.insert(arr[i])
		if arr[i] < heap.peek():
			h.remove()
			h.insert(arr[i])
	return h
