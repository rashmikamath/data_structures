def longest_palindrome(s):
	if len(s)%2==0:
		val = check_even_palindrome(s)
	else:
		val = check_odd_palindrome(s)
	return val

def check_odd_palindrome(s):
	longest = 1
	for i in range(len(s)):
		offset = 0
		while isvalid(s[i], i-1-offset) and isvalid(s[i], i+1+offset) and (s[i-1-offset]==s[i+1+offset]):
			offset += 1
		longestati = offset*2+1
		if longest<longestati:
			longest = longestati
			r
	return (i-1-offset,i+1+offset)

def check_even_palindrome(s):
	longest = 1
	for i in range(len(s)):
		offset = 0
		while isvalid(s[i], i-offset) and isvalid(s[i], i+1+offset) and (s[i-offset]==s[i+1+offset]):
			offset += 1
		longestati = offset*2
		if longest<longestati:
			longest = longestati

	return (i-offset,i+1+offset)

def isvalid(s, i):
	return i>=0 and i<len(s)

print(longest_palindrome("ab​babab​aab"))