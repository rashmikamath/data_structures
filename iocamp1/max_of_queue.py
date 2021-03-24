

class Queue():
	def __init__(self, arr=list()):
		self.arr = []
		

	def isEmpty(self):
		return self.arr == []

	def add_back(self, item):
		return self.arr.append(item)

	def get_back(self):
		return self.arr[0]

	def add_front(self, item):
		return self.arr.insert(0, item)

	def get_front(self):
		return self.arr[len(self.arr)-1]

	def delete_front(self):
		return self.arr.pop()

	def delete_back(self):
		return self.arr.pop(0)

	def size_q(self):
		return len(self.arr)

	def print_q(self):
		print(self.arr)	
	


def QueueMax(arr):
	main = Queue()
	max_queue = Queue()

	for i in range(len(arr)):
		main.add_back(arr[i])
		main.print_q()
		print("====Mainend+======")
		while (not max_queue.isEmpty() and max_queue.get_front() < arr[i]):
			max_queue.delete_back()
		max_queue.add_back(arr[i])
		max_queue.print_q()
		print("+++Maxend++++")

		if main.isEmpty():
			return
		return max_queue.get_front()
		

		if main.isEmpty():
			return
		item = main.delete_front()
		if max_queue.get_back() == item:
			max_queue.delete_front()

		
		

QueueMax([1,2,5,6,3,0])