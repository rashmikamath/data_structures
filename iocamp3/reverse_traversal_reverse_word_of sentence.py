def reverse_word(s):
	if len(s) == 0 or s==None:
		return -1 
	res = ''
	i = len(s)-1
	end = len(s)
	while i>0:
		if s[i] == " ":
			if len(res) > 0:
				res += ' '
			res += s[i+1:end]
			end = i 
		i -= 1
	first_word = s[0:end+1]
	if len(res) > 0:
		res += ' '
	res += first_word
	return res

print(reverse_word("i want to live in house"))