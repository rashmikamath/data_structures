class ArrayStack:
	def __init__(self):
		self.a = []
		self.s1 = 0
		self.s2 = len(self.a)-1

	def push(self, stack_num, item):
		if stack_num!=1 or stack_num!=2:
			print("Invalid")

		if self.s1>self.s2:
			print("Invalid")

		if stack_num==1:
			self.a[self.s1] = item
			self.s1 += 1
		elif stack_num==2:
			self.a[self.s2] = item
			self.s2 -= 1
		else:
			print("Invalid")

	def pop(self, stack_num):
		if stack_num!=1 or stack_num!=2:
			print("invalid")

		if stack_num==1 and self.s1>0:
			res = self.a[self.s1]
			self.s1 -= 1

		if stack_num==2 and self.s2<len(self.a)-1:
			res = self.a[self.s2]
			self.s2 += 1
		return res

	def print_stack(self):
		print(self.a)

s = ArrayStack()
s.push(1, 1)
s.push(2, 2)
s.push(1, 3)
s.push(2, 4)
s.print_stack()
s.pop(1)
s.print_stack()