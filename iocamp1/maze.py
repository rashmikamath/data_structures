def solvemaze(maze):
	memo = [["UNVISITED" for i in range(4)] for j in range(4)]
	if solvemazeutil(maze, 0, 0, memo):
		return True

def solvemazeutil(maze, i, j, memo):
	if oob(maze,i,j) or maze[i][j] == 1:
		return False

	if (i==3) and (j==3):
		return True

	if memo[i][j] == "PATH_NOT_FOUND" or memo[i][j] == "VISITING":
		return False
	memo[i][j] = "VISITING"
	points = [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]

	for p in points:
		print(p)
		if solvemazeutil(maze, p[0], p[1], memo):
			return True
	memo[i][j] = "PATH_NOT_FOUND"
	return False


def oob(maze, i, j):
	return (i < 0 ) or (i >= 4) or (j<0) or (j>=4)

if __name__ == "__main__":
	print(solvemaze([[0,1,1,1],[0,0,0,0],[1,1,1,0],[1,1,1,1]]))