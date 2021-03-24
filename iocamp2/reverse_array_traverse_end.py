def reverse_array(arr):
	if len(arr) == 0:
		return
	start = 0
	end = len(arr)-1
	while start <= end:
		swap(arr, start, end)
		start += 1
		end -= 1
	return arr

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr

print(reverse_array([1,2,3,4,5,6]))