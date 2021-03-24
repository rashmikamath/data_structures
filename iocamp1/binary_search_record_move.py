def binary_search(a, target):
	low = 0
	high = len(a)-1
	result = -1
	while(low<=high):
		mid = low + (high-low)//2
		
		result = record(a, mid, target, result)
		print("Res val", result)
		if a[mid] > target :
			high = mid-1
		elif a[mid] < target:
			low = mid+1
		else:
			return mid
	return result

def record(a, mid, target, result):
	if (result == -1) or (abs(a[mid]-target) < abs(a[result]-target)):
		return mid
	return result
print(binary_search([10,20,30,40], 5))
