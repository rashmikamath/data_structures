class Queue():
	def __init__(self, capacity):
		self.a = []
		self.front = 0
		self.back = 0
		self.length = 0
		self.capacity = capacity

	def add(self, n):
		if self.length == self.capacity:
			raise("Max length reached")
		self.a.append(n)
		self.back = (self.back+1)%len(self.a)
		self.length += 1

	def remove(self):
		if self.length == 0:
			raise("Queue is empty")
		result = self.a[0]
		del self.a[0]
		self.front = (self.front+1)%self.capacity
		self.length -= 1
		return result