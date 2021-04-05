def find_target(arr, target):
	
	high = 1
	last_index = -1
	while True:
		try:
			temp = arr[high]
		except:
			last_index = binary_search_last_index(arr, high//2, high)
		high = high*2
	return binary_search(arr, target, 0, last_index)

def binary_search_last_index(arr, low, high):
	while low<=high:
		mid = low+(high-low)//2
		try:
			temp = arr[mid]
		except:
			high = mid-1
			continue
		try:
			temp = arr[mid+1]
		except:
			return mid
		low = mid+1
	return -1

def binary_search(arr, target, low, high):
	while low<=high:
		mid = low+(high-low)//2
		if arr[mid] < target:
			low = mid+1
		elif arr[mid] > target:
			high = mid-1
		else:
			return mid 
	return -1

print(find_target([1,2,6,7,9,10,13,16,19,21,22,32,45,52,56,59,61,67,69,70], 7))