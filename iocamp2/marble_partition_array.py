marble_dictionary = {"red":0,"white":1, "blue":2}
def marble(arr):
	low_boundary = 0
	high_boundary = len(arr)-1
	i = 0
	while i <= high_boundary:
		if arr[i] == marble_dictionary.get("red"):
			swap(arr, i, low_boundary)
			low_boundary += 1
			i += 1
		elif arr[i] == marble_dictionary.get("blue"):
			swap(arr, i, high_boundary)
			high_boundary -= 1
		elif arr[i] == marble_dictionary.get("white"):
			i += 1
		else:
			raise NotImplementedError("Not implemented")
	return arr

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
	return a

print(marble([1,0,2,1,0,2,1,0,2]))