def min_insertion_palindrome(s):
	def lcs(st1, st2):
		m = len(st1)
		n = len(st2)
		dp = [[0 for i in range(n+1)] for j in range(m+1)]
		for i, s1 in enumerate(st1):
			for j, s2 in enumerate(st2):
				if s1==s2:
					dp[i+1][j+1] = 1+dp[i][j]
				else:
					dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
		return dp[-1][-1]
	return len(s)-lcs(s, s[::-1])

t = "zzazz"
print(min_insertion_palindrome(t))

t = "mbadm"
print(min_insertion_palindrome(t))

t = "leetcode"
print(min_insertion_palindrome(t))

t = "no"
print(min_insertion_palindrome(t))

t = "g"
print(min_insertion_palindrome(t))