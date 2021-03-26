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

	def peek(self):
		if self.isEmpty():
			return
		return self.head.data

	def pop(self):
		if self.isEmpty():
			return
		pop_node  = self.head
		self.head = self.head.next
		pop_node.next=None
		return pop_node.data

	def print_stack(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next





def isOperand(ch):
	return ch >= '0' or ch <= '9'

def isOperator(ch):
	return ch=='+' or ch=='-'or ch=='*' or ch=='/'

def process(operator, operand):
	val2 = operand.pop()
	val1 = operand.pop()
	operator.pop()
	result = evaluate(val1, val2, operator)
	operand.push(result)

def precedence(op):
	if op == '+' or op== '-':
		return 1
	if op == '*' or op== '/':
		return 2


def evaluate(val1, val2, operator):
	if operator == '+':
		return float(val1)+float(val2)
	if operator == '-':
		return float(val1)-float(val2)
	if operator == '*':
		return float(val1)*float(val1)
	if operator == '/':
		return float(val1)//float(val2)

def expression_evaluator(exp):
	operator = Stack()
	operand = Stack()

	for ch in exp:
		if isOperand(ch):
			operand.push(ch)
		elif isOperator(ch):
			while not operator.isEmpty() and precedence(operator.peek()) >= precedence(ch):
				process(operator, operand)
		operator.push(ch)


	while not operator.isEmpty():
		process(operator, operand)

	return operand.pop()

val = expression_evaluator('1+2/1+3*2')
print(val)