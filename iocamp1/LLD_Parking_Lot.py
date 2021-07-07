class Car:
	def __init__(self, registration_number, color):
		self.registration_number = registration_number
		self.color = color

	def get_registration_number(self):
		return self.registration_number

	def get_color(self):
		return self.color

class Slot:
	def __init__(self, slot_number, parked_car=None):
		self.parked_car = parked_car
		self.slot_number = slot_number

	def get_slot_number(self):
		return self.get_slot_number

	def get_parked_car(self):
		return self.slot_number

	def assign_car(self, car):
		self.parked_car = car

	def isSlotFree(self):
		return self.parked_car == None

	def unassign_car(self):
		self.parked_car = None

class ParkingLot:
	def __init__(self):
		self.max_capacity = 120
		self.slots = {i:Slot(i) for i in range(1,self.max_capacity)}
		


	def get_slots(self):
		return self.slots

	def get_capacity(self):
		return self.capacity

	def parking_lot(self, capacity):
		if capacity > self.max_capacity  or capacity < 0:
			raise ParkingLotCapacityError("Invalid value given for capapcity")
		self.capacity = capacity
		self.slots = dict()


	def get_slot(self, slot_number):
		if slot_number >= self.get_capacity() or slot_number <= 0:
			raise SlotNumberError()
		allslots = self.get_slots()
		if slot_number not in self.slots.keys():
			allslots[slot_number] = Slot(slot_number)
		return allslots.get(slot_number)

	def park(self, car, slot_number):
		slot = self.get_slot(slot_number)
		if not slot.isSlotFree():
			raise SlotNotFree()
		slot.assign_car(car)
		return slot

	def make_slot_free(self, slot_number):
		slot = self.get_slot(slot_number)
		slot.unassign_car()
		return slot_number

class ParkingLotCapacityError(Exception):
	pass
class SlotNumberError(Exception):
	pass
class SlotNotFree(Exception):
	pass
p = ParkingLot()
p.parking_lot(130)
print(p.get_slot(10))
p.park(Car("1234", "RED"), 10)
print(p.get_slot(10))
p.park(Car("123", "BLACK"), 102)
p.park(Car("123", "BLACK"), 11)

p.make_slot_free(10)
p.park(Car("124", "WHITE"), 10)




















