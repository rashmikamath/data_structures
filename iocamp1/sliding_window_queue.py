class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Queue_List():
	def __init__(self, front=None, back=None):
		self.back = back
		self.front = front

	def isEmpty(self):
		if self.front == None:
			return True
		else:
			return False

	def add(self, item):
		temp = Node(item)
		if self.back==None:
			self.back=self.front=temp
			return 
		self.back.next = temp
		self.back = temp

	def remove(self):
		if self.isEmpty():
			return 
		temp = self.front

		self.front = temp.next

		if self.front==None:
			self.back=None
		return temp.data

	def size(self):
		temp = self.front
		count = 0
		while temp is not None:
			count += 1
			temp = temp.next
		return count

	def print_queue(self):
		temp = self.front
		while temp is not None:
			print(temp.data)
			temp = temp.next

class Queue_Array:
	def __init__(self, capacity, arr=[]):
		self.arr = arr
		self.capacity = capacity
		self.front = 0
		self.rear = 0

	def add(self, item):
		if self.capacity == self.rear:
			print("Queue is full")
		self.arr.append(item)
		self.rear += 1

	def remove(self):
		if self.front == self.rear:
			print("Queue is empty")
		last = self.arr.pop(0)
		self.rear -= 1
		return last

	def size(self):
		if self.front == self.rear:
			print("Queue is empty")
		count = 0

		for i in self.arr:
			count += 1
		return count

	def print_queue(self):
		if self.front == self.rear:
			print("Queue is empty")
		for i in self.arr:
			print(i)

def sliding_window(arr, k):
	if arr==None or k==0 or len(arr)==0:
		return

	sum_queue = 0
	#q = Queue_List()
	q1 = Queue_Array(k)
	
	for i in range(len(arr)):
		if q1.size() == k:
			last = q1.remove()
			try:
				sum_queue -= last
			except:
				import pdb
				pdb.set_trace()
		q1.add(arr[i])
		q1.print_queue()
		print("=====")
		sum_queue += arr[i]
		if q1.size() == k:
			print(sum_queue)
			print("===Sum===")
			

sliding_window([2,3,5,6,2,1],3)