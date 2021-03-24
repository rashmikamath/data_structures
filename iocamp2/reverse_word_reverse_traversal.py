def reverse_word(s):
	word_index = len(s)
	i = len(s)-1
	res = ''
	while i >=0:
		if s[i] == " ":
			if len(res) > 0:
				res += ' '
			res += s[i+1:word_index]
		
			word_index = i
		i -= 1

	first_word = s[0:word_index]
	if len(res) > 0:
		res += ' '
	res += first_word
	return res

print(reverse_word("i live in a house"))
