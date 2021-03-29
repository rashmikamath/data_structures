def copy_even_twice(arr):
	if len(arr)==0 or arr==None:
		return -1
	number_index = get_number(arr)
	end = len(arr)
	while number_index >= 0:
		if arr[number_index]%2==0:
			end -= 1
			arr[end] = arr[number_index]
		end -= 1
		arr[end] = arr[number_index]
		number_index -= 1
	return arr


def get_number(arr):
	end = len(arr)-1
	while end >= 0 and arr[end] == -1:
		end -= 1
	return end

print(copy_even_twice([2,4,1,0,3, -1,-1,-1]))
