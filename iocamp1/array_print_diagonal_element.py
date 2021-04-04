def print_arr_diagonary(arr):
	row = 0
	col = 0
	up = True

	while True:
		print(arr[row][col])
		if (row==0 or row==len(arr)-1) and col != len(arr[0])-1:
			
			col += 1
			print(arr[row][col])
			up = not up
		if col == 0 or col==len(arr[0])-1:
			
			row += 1
			print(arr[row][col])
			up = not up
		

		if row == len(arr)-1 and col == len(arr[0])-1:
			break

		if row == up:
			row = row-1
		else:
			row = row+1

		if col == up:
			col = col+1
		else:
			col = col-1

print(print_arr_diagonary([[1,2,3,4],[5,6,7,8],[9,0,1,2]]))