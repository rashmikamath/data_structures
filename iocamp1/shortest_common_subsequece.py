def scs(str1, str):
	m = len(str1)
	n = len(str2)
	dp = [[0 for i in range(n+1)] for j in range(m+1)]
	for i, s1 in enumerate(str1):
		for j, s2 in enumerate(str2):
			if s1==s2:
				dp[i+1][j+1] = 1+dp[i][j]
			else:
				dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
	seq = []
	i = m-1
	j = n-1
	while i >=0 and j >= 0 :
		if s1[i] == s2[j]:
			seq.append(s[i])
			i -= 1
			j -= 1
		elif dp[i+1][j] < dp[i][j+1]:
			seq.append(s1[i])
			i -= 1
		else:
			seq.append(s1[j])
			j -= 1
	return s1[:i+1]+s2[:j+1]+''.join(reversed(seq))
	
str1 = "abac"
str2 = "cab"
print(scs(str1, str2))