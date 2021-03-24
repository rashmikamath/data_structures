def sub_array_sum(arr, target):
	start = 0
	end = 0
	arr_sum = arr[0]
	while start <= len(arr)-1:
		if start > end:
			end  = start
			arr_sum = arr[start]
		if arr_sum < target:
			if end == len(arr)-1:
				break
			end  += 1
			arr_sum += arr[end]
		elif arr_sum > target:
			arr_sum -= arr[start]
			start += 1
		else:
			return (arr[start], arr[end])

print(sub_array_sum([1,2,3,5,2], 8))