def print_subset(arr, k):
	if len(arr)==0 or arr==None or k==None:
		return 
	buff = [0]*k
	print_subset_helper(arr, buff, 0, 0)

def print_subset_helper(arr, buff, start_index, buff_index):
	print(buff[:buff_index])
	#terminatination case
	if buff_index==len(buff) :
		return 

	if start_index==len(arr):
		return

	#find candidate
	for i in range(start_index, len(arr)):
		buff[buff_index] = arr[i]
		print_subset_helper(arr, buff, i+1, buff_index+1)

print_subset([1,2,3,4,5],3)