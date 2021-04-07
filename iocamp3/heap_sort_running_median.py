class RunningMedian:
	def __init__(self):
		low = MaxHeap()
		high = MinHeap()

	def get_median(self):
		if low.size()==0 and high.size()==0:
			return 

		if low.size() == hig.size():
			return low.peek()+(high.peek()-low.peek())//2
		return high.peek()

	def insert(self, number):
		if number==None:
			return

		if high.size() == 0:
			high.add(number)

		if low.size()==high.size():
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
		