def rotate_array_by_90(arr):
	if len(arr)==0 or arr==None or len(arr[0])!=len(arr) :
		return arr
	size = len(arr)
	for i in range(0,size//2):
		r1 = i
		c1 = i
		r2 = size-r1-1
		c2 = size-r2-1
		for j in range(1, (c2-c1)+1):
			print(j)
			import pdb
			pdb.set_trace()
			perform_move(arr, r1, c1, r2, c2, j)
	return arr

def perform_move(arr, r1, c1, r2, c2, offset):
	temp = arr[r1][c1+offset]
	arr[r1][c1+offset] = arr[r1+offset][c2]
	arr[r1+offset][c2] = arr[r2-offset][c1]
	arr[r2-offset][c1] = arr[r2][c2-offset]
	arr[r2][c2-offset] = temp

print(rotate_array_by_90([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
