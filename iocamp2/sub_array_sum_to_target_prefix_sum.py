def sub_array_sum_target(arr, target):
	if len(arr) == 0:
		return 0

	arr_sum = 0
	arr_dict = {}
	for i in range(0, len(arr)):
		arr_sum += arr[i]
		if arr_sum == target:
			return arr[0:i+1]
		if arr_sum in arr_dict.keys():
			return arr[arr_dict[(arr_sum)-target]+1:i+1]

		arr_dict[(arr_sum)-target] = i
	return -1

print(sub_array_sum_target([2,4,-2,1,-3,5,-3], 5))