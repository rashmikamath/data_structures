def sub_array(arr):
	res = arr[0]
	max_end = arr[0]
	max_index = 0
	for i in range(1, len(arr)):
		max_end = max(arr[i], max_end+arr[i])
		if max_end > res:
			res = max_end
			max_index = i
	res_list = []
	while res > 0:
		res_list.append(arr[max_index])
		res -= arr[max_index]
		max_index -= 1
	return res_list[::-1]

print(sub_array([1,2,-1,2,-3,2,-5]))