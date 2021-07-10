class VendingMachine:
	def __init__(self, )
class Inventory:
	def __init__(self):
		self.inventory = dict()

	def get_quantity(self, item):
		value = self.inventory.get(item)
		if value == None:
			return 0
		else:
			return value

	def add_item(self, item):
		count = self.inventory(item)
		self.inventory[item] = count+1

	def delete_item(self, item):
		if item in self.inventory:
			count = self.inventory[item]
			self.inventory[item] = count-1

	def hasItem(self, item):
		return self.inventory[item] > 0


	def put_item(self, item, quantity):
		self.inventory[item] = quantity

class Item:
	def __init__(self, name, price):
		self.name = name
		self.price = price


