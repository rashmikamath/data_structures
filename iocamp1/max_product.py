def max_product(arr1, arr2):
	m = len(arr1)
	n = len(arr2)
	mx = float("-inf")
	dp = [[0 for i in range(n+1)] for j in range(m+1)]
	for i, n1 in enumerate(arr1):
		for j, n2 in enumerate(arr2):
			p = n1*n2
			mx = max(mx, p)
			p = max(p, 0)
			dp[i+1][j+1] = max(dp[i][j]+p, dp[i][j+1], dp[i+1][j])
	return mx if mx<=0 else dp[-1][-1]

print(max_product([2,1,-2,5],[3,0,-6]))

print(max_product([3,-2],[2,-6,7]))

print(max_product([-1,-1],[1,1]))