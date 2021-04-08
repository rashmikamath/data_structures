def rotate_array_90(arr):
	if len(arr)==0 or arr==None or len(arr[0])!=len(arr) :
		return arr

	size = len(arr)
	print(size)
	for ix in range(0, (size//2)):
		r1 = ix
		c1 = ix
		r2 = size-r1-1
		c2 = size-r1-1
		for jx in range(1, (c2-c1)+1):
			perform_move(arr, r1, c1, r2, c2, jx)
			
	return arr

def perform_move(arr, r1, c1, r2, c2, offset):
	temp = arr[r1][c1+offset]
	arr[r1][c1+offset] = arr[r2-offset][c1]
	arr[r2-offset][c1] = arr[r2][c2-offset]
	arr[r2][c2-offset] = arr[r1+offset][c2]
	arr[r1+offset][c2] = temp

print(rotate_array_90([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

