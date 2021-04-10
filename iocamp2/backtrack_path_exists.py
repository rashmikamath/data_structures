def pathexists(arr):
	if len(arr)==0 or arr==None:
		return
	memo = [["UNVISITED" for i in range(len(arr[0])-1)] for j in range(len(arr)-1)]
	pathexists_helper(arr, 0, 0, memo)

def pathexists_helper(arr, i, j, memo):
	if oob(i,j) or arr[i][j]==1:
		return False

	if i==len(arr)-1 and j==len(arr[0]-1):
		return True

	if memo[i][j]=="VISITING" or memo[i][j]=="PATH_NOT_FOUND":
		return False

	memo[i][j] = "VISITING"
	points = [[i+1,j], [i-1, j], [i, j+1], [i, j-]]
	for point in points:
		pathexists_helper(arr, point[0], point[1], memo)
		return True

	memo[i][j] = "PATH_NOT_FOUND"
	return False

print(pathexists())