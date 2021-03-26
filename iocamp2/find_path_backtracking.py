
memo = [["UNVISITED" for j in range(5)] for i in range(5)]

def path_exist(arr, i, j, memo):
	if oob(i, j) or arr[i][j] == 1:
		return False

	if i==len(arr)-1 and j==len(arr[0])-1:
		return True

	if memo[i][j]=="VISITING" or memo[i][j] =="PATH_NOT_FOUND":
		return False

	memo[i][j] = "VISITING"
	pair = [[i, j+1],[i,j-1],[i+1,j],[i-1,j]]
	for p in pair:
		if path_exist(arr, p[0],p[1], memo):
			return True
	memo[i][j] = "PATH_NOT_FOUND"
	return False

def oob(i,j):
	return i<0 or i>=5 or j<0 or j >=5

print(path_exist([[0,1,0,0,0],[0,1,0,1,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,1,0]], 0, 0 ,memo))