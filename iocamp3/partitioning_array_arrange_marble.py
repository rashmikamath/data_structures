d = {"white":1, "red":0, "blue":2}
def arrange_marble(arr):
	low_boundary = 0
	high_boundary = len(arr)-1
	i = 0
	while i<=high_boundary:
		if arr[i]==d.get("red"):
			swap(arr, i, low_boundary)
			low_boundary += 1
			i += 1
		elif arr[i] == d.get("blue"):
			swap(arr, i, high_boundary)
			high_boundary -= 1
		elif arr[i]==d.get("white"):
			i += 1
	return arr
		
def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp
	return arr

print(arrange_marble([1,2,0,1,2,0,1,2,0,1,2,0]))