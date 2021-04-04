def sub_array_sum_to_zero(arr):
	prefix_sum=0
	map_dict = dict()
	for i in range(len(arr)):
		prefix_sum += arr[i]
		if prefix_sum == 0:
			return arr[0:i+1]
		if prefix_sum in map_dict.keys():
			return arr[map_dict.get(prefix_sum)+1:i+1]
		map_dict[prefix_sum] = i 
	return arr

print(sub_array_sum_to_zero([2,4,-2,1,-3,5,-3]))