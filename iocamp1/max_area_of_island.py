def max_area_of_island(grid):
	if not grid:
		return 
	max_area = 0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				max_area = max(max_area, dfs(grid, i, j))
	return max_area

def dfs(grid, i, j):
	if not oob(grid, i, j) and grid[i][j]==1:
		grid[i][j]=0
		return 1+dfs(grid, i, j+1)+dfs(grid, i, j-1)+dfs(grid, i+1, j)+dfs(grid, i-1, j)
	return 0

def oob(grid, i, j):
	return i <0 or i>=len(grid) or j < 0 and j >= len(grid[0])

print(max_area_of_island([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
	[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
