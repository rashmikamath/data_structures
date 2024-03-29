def edit_distane(s, t):
	m = len(s)
	n = len(t)

	dp = [[0 for i in range(n+1)] for j in range(m+1)]
	for i in range(n+1):
		dp[0][i] = i

	for i in range(m+1):
		dp[i][0] = i

	for i in range(1, m+1):
		for j in range(1, n+1):

			if s[i-1] == t[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
			print(dp)
	return dp[-1][-1]

print(edit_distane("horse", "ros"))
print(edit_distane("intention", "execution"))