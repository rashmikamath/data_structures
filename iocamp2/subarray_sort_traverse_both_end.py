def sort_subarray(arr):
	minimum = 0
	maximum = float("inf")
	if len(arr) == 0:
		return 0

	#Find Dip
	for start in range(0, len(arr)):
		if arr[start+1] > arr[start]:
			break
	if start == len(arr)-1:
		return

	#Find rise
	for end in range(len(arr)-1, 0, -1):
		if arr[end-1] > arr[end]:
			break

	for k in range(start, end+1):
		if arr[k] > maximum:
			maximum = arr[k]
		if arr[k] < minimum:
			minimum = arr[k]

	while start > 0 and arr[start-1] > minimum:
		start -= 1
	while end < len(arr)-1 and arr[end+1] < maximum:
		end += 1
	return start, end

print(sort_subarray([1,2,4,5,3,5,6,7]))