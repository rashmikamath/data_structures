def number_closed_island(grid):
	print(grid)
	if not grid:
		return
	hash_map = set()
	res = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 0 and (i, j) not in hash_map:
				val = dfs(grid, i, j, hash_map)
				res += 1 if val else 0
				
	return res

def dfs(grid, i, j, hash_map):
	if oob(grid, i, j):
		return False

	if (i, j) in hash_map:
		return True

	if grid[i][j] == 1:
		return True

	hash_map.add((i, j))
	right = dfs(grid, i+1, j, hash_map)
	left = dfs(grid, i-1, j, hash_map)
	top = dfs(grid, i, j+1, hash_map) 
	bottom = dfs(grid, i, j-1, hash_map)
	return right and left and top and bottom

def oob(grid, i, j):
	return i < 0 or i >= len(grid) or j < 0 or j >=len(grid[0])

val = number_closed_island([[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]])
print(val)
