def distinct_subsequence(s, t):
	m = len(s)
	n = len(t)
	dp = [[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(m+1):
		dp[0][i] = 1


	for i, t1 in enumerate(t):
		for j, s1 in enumerate(s):
			if t1 == s1:
				dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
			else:
				dp[i+1][j+1] = dp[i+1][j]
	return dp[len(t)][len(s)]
s = "rabbbit"
t = "rabbit"
print(distinct_subsequence(s, t))
s = "babgbag"
t = "bag"
print(distinct_subsequence(s, t))