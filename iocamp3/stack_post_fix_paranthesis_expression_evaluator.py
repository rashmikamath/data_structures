def paranthesis_expression_evaluator(s):
	operator = Stack()
	operand = Stack()
	for ch in s:
		if isOperand(ch):
			operand.push(ch)
		elif isOperator(ch):
			# import pdb
			# pdb.set_trace()
			while not operator.isEmpty() and precedence(operator.peek()) >= precedence(ch):
				process(operator, operand)
			operator.push(ch)
		elif ch=='(':
			operator.push(ch)
		elif ch == ')':
			while not operator.peek()=='(':
				process(operator, operand)
			operator.pop()
		else:
			print("Invalid Operation")
	while not operator.isEmpty():
		process(operator, operand)
	return operand.pop()

def isOperand(ch):
	return ch >= '0' and ch<='9'

def isOperator(ch):
	return ch == "+" or ch== '*' or ch=='/' or ch=='-'

def precedence(ch):
	if ch=='*' or ch=='/':
		return 2
	elif ch=='+' or ch=='-':
		return 1
	elif ch==')' or ch=='(':
		return 0
	else:
		print("Invalid Predence")

def process(operator, operand):
	num2 = operand.pop()
	num1 = operand.pop()
	res = apply_func(num1,num2,operator.pop())
	operand.push(str(res))

def apply_func(num1, num2, operator_ch):
	if operator_ch=='+':
		res = float(num1)+float(num2)
	elif operator_ch == '-':
		res = float(num1)-float(num2)
	elif operator_ch == '*':
		res = float(num1)*float(num2)
	elif operator_ch == '/':
		res = float(num1)/float(num2)
	else:
		print("Not an operator")
	return res
class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


class Stack:
	def __init__(self, head=None):
		self.head = head

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	def push(self, item):
		if self.head == None:
			self.head = Node(item)
		else:
			new_node = Node(item)
			new_node.next = self.head
			self.head = new_node

	def pop(self):
		if self.isEmpty():
			return
		pop_node = self.head
		self.head = self.head.next
		pop_node.next = None
		return pop_node.data

	def peek(self):
		if self.isEmpty():
			return
		return self.head.data

	def print_s(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next

print(paranthesis_expression_evaluator("1+(2/1)+(3*2)"))