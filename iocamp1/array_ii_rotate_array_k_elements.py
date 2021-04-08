def rotate_array(arr, k):
	if arr==None or len(arr)== 0 or k==None:
		return

	reverse_arr(arr, 0, len(arr)-1)
	reverse_arr(arr, 0, k-1)
	reverse_arr(arr, k, len(arr)-1)
	return arr

def reverse_arr(arr, start, end):
	while start<end:
		swap(arr, start, end)
		start += 1
		end -= 1
	return arr

def swap(arr, start, end):
	temp = arr[start]
	arr[start] = arr[end]
	arr[end] = temp

print(rotate_array([1,2,3,4,5,6], 2))

