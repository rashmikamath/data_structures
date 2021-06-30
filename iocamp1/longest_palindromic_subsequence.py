def longest_palindromic_subsequence(s):
	n = len(s)
	dp = [[0 for i in range(n)] for j in range(n)]
	for i in range(n-1, -1, -1):
		print(i)
		dp[i][i] = 1
		for j in range(i+1, len(s)):
			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1]+2
			else:
				dp[i][j] = max(dp[i][j-1], dp[i+1][j])
	print(dp)
	return dp[0][-1]
print(longest_palindromic_subsequence("bbbab"))