dirs = [[0,1], [1, 0], [0,-1], [-1, 0]]
def longest_path_matrix_sum(matrix):
	if not matrix:
		return
	m = len(matrix)
	n = len(matrix[0])
	max_val = 1
	cache = [[0 for i in range(n)] for j in range(m)]
	for i in range(n):
		for j in range(m):
			max_val = max(max_val, dfs(matrix, i, j, m, n, cache))
	return max_val


def dfs(matrix, i, j, m, n, cache):
	if cache[i][j]!=0:
		return cache[i][j]
	max_val = 1
	for d in dirs:
		x = i+d[0]
		y = j+d[1]
		if oob(matrix, x, y) or matrix[x][y] <= matrix[i][j]:
			continue
		len_val = 1+dfs(matrix, x, y, m, n, cache)
		max_val = max(max_val, len_val)
	cache[i][j] = max_val
	return max_val

def oob(matrix, i, j):
	return i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])
print(longest_path_matrix_sum([[9,9,4],[6,6,8],[2,1,1]]))