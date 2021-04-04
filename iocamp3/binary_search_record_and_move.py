def binary_search(arr, target):
	low = 0
	high = len(arr)-1
	res = -1
	while low <= high:
		mid = low + (high-low)//2
		res = record(arr, mid, target, res)
		if arr[mid] > target:
			high = mid -1
		elif arr[mid] < target:
			low = mid+1
		else:
			return mid
	return res

def record(arr, mid, target, res):
	if res == -1 or (abs(arr[mid]-target)< abs(arr[res]-target)):
		return mid
	return res

print(binary_search([10,20,30,40,50], 23))