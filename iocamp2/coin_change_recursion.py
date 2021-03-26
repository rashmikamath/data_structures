def print_coin_change(coins, target):
	if len(coins)==0 or coins==None or target==None:
		return 
	print_coin_change_helper(coins, target, Stack(), 0, 0)

def print_coin_change_helper(coins, target, buffer, start_index, curr_sum):
	if curr_sum > target:
		return

	if curr_sum==target:
		print("++++++++++")
		buffer.print_stack()
		print("+++++++++++")
		return 

	for i in range(start_index, len(coins)):
		
		buffer.push(coins[i])
		print_coin_change_helper(coins, target, buffer, i, curr_sum+coins[i])
		
		buffer.pop()
		
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
		if self.head==None:
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

	def print_stack(self):
		print_val = self.head
		while print_val is not None:
			print(print_val.data)
			print_val = print_val.next

print_coin_change([1,2,5], 5)
