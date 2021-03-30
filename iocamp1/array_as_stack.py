class ArrayAsStack:
	def  __init__(self):
		self.a = []
		self.s1 = 0
		self.s2 = len(self.a)-1

	def push(self, stack_num, item):
		
		if stack_num != 1 or stack_num !=2:
			raise ("Improper stack number")
		if self.s1 > self.s2:
			raise ("Array is full")
		if stack_num == 1:
			self.a[s1] = item
			self.s1 += 1
		else:
			self.a[self.s2] = item
			self.s2 -= 1

	def pop(self, stack_num):
		if stack_num != 1 or stack_num !=2:
			raise("Improper stack nuber")
		if stack_num == 1 and self.s1 > 0:
			val = a[s1]
			s1 -= 1
			return val
		if stack_num == 2 and self.s2 < len(self.a)-1:
			val = a[s2]
			s2 += 1
			return val

	def print_stack(self):
		print(self.a)

s = ArrayAsStack()
s.push(1, 1)
s.push(2, 2)
s.push(1, 3)
s.push(2, 4)
s.print_stack()
s.pop(1)
s.print_stack()