def countigous_subarray_sort(arr):
	if len(arr)==0 or arr==None:
		return -1

	for start in range(0, len(arr)):
		if arr[start]>arr[start+1]:
			break

	if start == len(arr):
		return -1

	for end in range(len(arr)-1, -1, -1):
		if arr[end-1] < arr[end]:
			break

	min_val = float("inf")
	max_val = float("-inf")

	for k in range(start, end+1):
		if arr[k] < min_val:
			min_val = arr[k]
		if arr[k] > max_val:
			max_val = arr[k]

	while start > 0 and arr[start-1] > min_val:
		start -= 1

	while end < len(arr)-1 and arr[end+1] < max_val:
		end += 1
	return start,end

print(countigous_subarray_sort([1,3,5,2,6,4,7,8,9]))