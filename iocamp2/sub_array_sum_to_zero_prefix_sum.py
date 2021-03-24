def sub_array_sum_zero(arr):
	if len(arr) == 0:
		return 
	arr_dict = {}
	arr_sum = 0
	for i in range(0, len(arr)):
		arr_sum += arr[i]
		if arr_sum == 0:
			return arr[0:i+1]
		if arr_sum in arr_dict.keys():
			return arr[arr_dict[arr_sum]+1:i+1]
		arr_dict[arr_sum] = i

	return None

print(sub_array_sum_zero([2,4,-2,1,-3,5,-3]))