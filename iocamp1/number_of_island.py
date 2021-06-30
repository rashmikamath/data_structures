def number_of_island(grid):
	print(grid)
	if not grid:
		return
	count = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]=="1":
				dfs(grid, i, j)
				count += 1
	return count

def dfs(grid, i, j):
	if oob(grid, i, j) or grid[i][j]!="1":
		return 
	grid[i][j] = "#"
	dfs(grid, i, j+1)
	dfs(grid, i, j-1)
	dfs(grid, i+1, j)
	dfs(grid, i-1, j)
	dfs(grid, i-1, j-1)
	dfs(grid, i-1, j+1)
	dfs(grid, i+1, j-1)
	dfs(grid, i+1, j+1)

def oob(grid, i, j):
	return i<0 or i>=len(grid) or j < 0 or j>=len(grid[0])

val = number_of_island([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(val)