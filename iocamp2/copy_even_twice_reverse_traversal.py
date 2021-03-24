def clone_even_number(arr):
	if len(arr)==0:
		return
	end = len(arr)
	i = get_last_number(arr)
	while(i>=0):
		if arr[i]%2==0:
			end -= 1
			arr[end] = arr[i]
		end -= 1
		arr[end] = arr[i]
		i -= 1
	return arr

def get_last_number(arr):
	i = len(arr)-1
	while( i>=0 and arr[i]==-1):
		i -= 1
	return i 

print(clone_even_number([2,0,4,1,3,-1,-1,-1]))