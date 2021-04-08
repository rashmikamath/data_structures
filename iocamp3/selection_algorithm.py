import random

def selection_algo(arr, k):
	if arr==None or len(arr)==0 or k==None:
		return

	target_index = k-1
	selection_algo_helper(arr, target_index, 0, len(arr)-1)

def selection_algo_helper(arr, target_index, start, end):
	
	random_index = get_random(start, end)
	pivot_index = partition(arr, start, end, random_index)
	if target_index == pivot_index:
		return arr[target_index]
	elif target_index < pivot_index:
		selection_algo_helper(arr, target_index, start, pivot_index-1)
	elif target_index > pivot_index:
		selection_algo_helper(arr, target_index-pivot_index-1, pivot_index+1, end)

def partition(arr, start, end, pivot_index):
	swap(arr, start, pivot_index)
	less = start
	for i in range(start+1, len(arr)):
		if arr[i]<=arr[start]:
			swap(arr, less+1, i)
	swap(arr, start, pivot_index)
	return pivot_index

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def get_random(start, end):
	return random.choice(list(range(start, end+1)))

print(selection_algo([7,6,5,4,3,2,1],3))