def square_arr(arr):
	if len(arr) == 0 or arr==None:
		return -1
	start = 0
	end = len(arr)-1
	res_index = len(arr)-1
	res = [0]*(len(arr))
	while start<end:
		if abs(arr[start]) < abs(arr[end]):
			res[res_index] = square(arr[end])
			end -= 1
		else:
			res[res_index] = square(arr[start])
			start += 1
		res_index -= 1
	return res

def square(val):
	return val*val

print(square_arr([-4,-2,0,1,3,5]))