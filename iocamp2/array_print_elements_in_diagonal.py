def print_diagonal(arr):
	if arr==None or len(arr)==0:
		return
	row = 0
	col = 0
	up = True

	while True:
		print(arr[row][col])
		if (row==0 or row==len(arr)-1) and col != len(arr[0])-1:
			print(arr[row][col])
			col += 1
			up = not up
		if col==0 or col == len(arr[0])-1:
			print(arr[row][col])
			row += 1
			up = not up

		if row == len(arr)-1 and col==len(arr[0])-1:
			break

		if up:
			row = row-1
		else:
			row =row+1

		if up:
			col = col+1
		else:
			col = col-1

