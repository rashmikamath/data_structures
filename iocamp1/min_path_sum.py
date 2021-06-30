def min_path_sum(arr):
	m = len(arr)
	n = len(arr[0])

	for i in range(1, m):
		arr[i][0] += arr[i-1][0]

	for j in range(1, n):
		arr[0][j] += arr[0][j-1]

	for i in range(1, m):
		for j in range(1, n):
			arr[i][j] += min(arr[i-1][j] , arr[i][j-1])
	return arr[-1][-1]

print(min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
print(min_path_sum([[1,2,3],[4,5,6]]))