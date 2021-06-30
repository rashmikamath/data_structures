def word_break(s, worddict):
	dp = [False]*(len(s)+1)
	dp[0] = True
	for i in range(1, len(s)+1):
		for j in range(0, i):
			if dp[j] and s[j:i] in worddict:
				dp[i] = True
				break
	print(dp)
	return dp[-1]
s = "leetcode"
wordDict = ["leet","code"]
print(word_break(s, wordDict))