def square_sort(arr):
	if len(arr) == 0:
		return 
	start = 0
	end = len(arr)-1
	result = [0]*len(arr)
	res_index = len(arr)-1
	while start<=end:
		if abs(arr[start]) > abs(arr[end]):
			result[res_index] = square(arr[start])
			start += 1
		else:
			result[res_index] = square(arr[end])
			end -= 1
		res_index -= 1
	return result
	
def square(i):
	return i*i

print(square_sort([-4,-2,-1,0,3,5]))