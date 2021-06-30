def lcs(str1, str2):
	m = len(str1)
	n = len(str2)
	dp = [[0 for i in range(n+1)] for j in range(m+1)]
	for i, s1 in enumerate(str1):
		for j, s2 in enumerate(str2):
			if s1 == s2:
				dp[i+1][j+1] = 1+dp[i][j]
			else:
				dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
	return dp[-1][-1]

text1 = "abcde"
text2 = "ace" 
print(lcs(text1, text2))
text1 = "abc"
text2 = "abc" 
print(lcs(text1, text2))
text1 = "abc"
text2 = "def" 
print(lcs(text1, text2))