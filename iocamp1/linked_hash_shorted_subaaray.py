def shortest_sub_array(doc, s):
	res = ''
	map_dict = dict()
	ll = LinkedList()

	for index, word in enumerate(doc):
		if word not in s:
			continue

		if word in map_dict.keys():
			node = map_dict.get(word)
			ll.delete_node(node)
		new_node = Node(word, index)
		ll.append(new_node)
		map_dict.setdefault(word, index)

		if len(map_dict) == len(s):
			end = ll.tail.index+len(word)-1
			start = ll.head.index
			if end-start+1< len(res):
				res = doc[start:end+1]
	return res

class LinkedList:
	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def isEmpty(self):
		if self.head==None:
			return True
		else:
			return False

	def append(self, append_node):
		if self.head==None:
			self.head = append_node
		else:
			self.tail = self.tail.set_next(append_node)
		self.tail = append_node

	def delete_node(self, toDelete, prev):
		if toDelete==None:
			return
		if toDelete==self.head:
			self.head = toDelete.next 
		if toDelete==self.tail:
			self.tail = prev
		if prev is not None:
			prev.next=toDelete.next 

	def delete(self, toDelete):
		next = toDelete.next
		if next is None:
			return
		toDelete.set_data(next.get_data())
		self.delete_node(next, toDelete)

	def print_ll(self):
		temp = self.head
		while temp is not None:
			print(temp.data)
			temp = temp.next

class Node:
	def __init__(self, word, index, next=None):
		self.word = word
		self.index = index
		self.next = next

	def get_next(self):
		return self.next

	def set_next(self, node):
		self.next = node

class WordIterator:
	def __init__(self, s, position=0):
		self.position = position
		self.s = s.split()

	def advance_to_next_alphabet(self):
		while self.position < len(self.s) and not 
