class RunningMedian:
	def __init__(self):
		low = MaxHeap()
		high = MinHeap()

	def get_median(self):
		if low.size() == 0 and high.size()==0:
			raise Exception
		if low.size()==high.size():
			return low.peek()+(high.peek()-low.peek())//2
		return high.peek()

	def insert(self, number):
		if high.isEmpty():
			high.add(number)

		if high.size() == low.size():
			if number < low.peek():
				high.add(low.remove())
				low.add(number)
			else:
				high.add(number)
		else:
			if number > high.peek():
				low.add(high.remove())
				high.add(number)
			else:
				low.add(number)