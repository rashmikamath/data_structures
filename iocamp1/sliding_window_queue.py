class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class Queue():
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


def sliding_window(arr, k):
	if arr==None or k==0 or len(arr)==0:
		return

	sum_queue = 0
	q = Queue()

	for i in range(len(arr)):
		if q.size() == k:
			last = q.remove()

			sum_queue -= last
		q.add(arr[i])
		q.print_queue()
		print("=====")
		sum_queue += arr[i]
		if q.size() == k:
			print(sum_queue)
			print("===Sum===")
			

sliding_window([2,3,5,6,2,1],3)