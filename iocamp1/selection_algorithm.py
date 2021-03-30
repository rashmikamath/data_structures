def kth_small_element_helper(a, target_index, start, end):
	random_index = get_random_index(a, start, end)
	pivot_index = partition(a, start, end, random_index)
	if target_index==pivot_index:
		return a[target_index]
	elif target_index < pivot_index:
		kth_small_element_helper(a, target_index, start, pivot_index-1)
	else:
		kth_small_element_helper(a, target_index-pivot_index-1, pivot+1, end)

def partition(a, start, end, pivot_index):
	swap(a[start], a[pivot_index])
	less = start
	for i in range(start+1, end+1):
		swap(a[i], a[less+1])
		less += 1
	swap(a[less], a[start])
	return less

def kth_small_element(a, target_index):
	val = kth_small_element_helper(a, target_index, 0, len(a))
	return val 

print(kth_small_element([5,7,4,6,5,3,3],3))