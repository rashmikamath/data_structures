def reverse_array(arr):
	if len(arr) == 0 or arr==None:
		return -1
	start=0
	end = len(arr)-1
	while start<=end:
		swap(arr, start, end)
		start += 1
		end -= 1
	return arr

def swap(arr, start, end):
	temp = arr[start]
	arr[start] = arr[end]
	arr[end] = temp
	return arr

print(reverse_array([1,2,3,4,5]))