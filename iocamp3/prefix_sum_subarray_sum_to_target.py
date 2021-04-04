def subarray_sum_to_target(arr, target):
	prefix_sum = 0
	map_dict = dict()
	for i in range(len(arr)):
		prefix_sum += arr[i]
		if prefix_sum==target:
			return arr[0:i+1]
		if (prefix_sum-target) in map_dict.keys():
			return arr[map_dict.get(prefix_sum-target)+1:i+1]
		map_dict[(prefix_sum-target)] = i

print(subarray_sum_to_target([2,4,-2,1,-3,5,-3], 5))