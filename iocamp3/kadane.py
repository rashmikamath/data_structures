def kadane_algorithm(arr):
	max_res = arr[0]
	max_end = arr[0]
	for i in range(1, len(arr)):
		max_end = max(max_end+arr[i], arr[i])
		if max_end > max_res:
			max_res = max_end
			max_index = i 
	res = []
	while max_res > 0:
		res.append(arr[max_index])
		max_res -= arr[max_index]
		max_index -= 1
	return res[::-1]

print(kadane_algorithm([1,2,-1,2,-3,2,-5]))
