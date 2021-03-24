def record_move(arr, target):
	low = 0
	high = len(arr)-1
	res = -1
	while low<=high:
		mid = low+(high-low)//2
		res = record(arr, mid, target, res)
		if arr[mid] > target:
			high  = mid-1
		elif arr[mid] < target:
			low = mid+1
		else:
			return mid
	return res



def record(arr, mid, target, res):
	if (abs(arr[mid]-target) < abs(res-target)) or res==-1:
		res = mid
	return res

print(record_move([10,20,30,40,50], 43))
