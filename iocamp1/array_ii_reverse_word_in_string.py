def reverse_word(s):
	import pdb
	pdb.set_trace()
	reverse_char(s, 0, len(s)-1)
	word_start = 0
	for i in range(len(s)):
		if s[i+1]== " ":
			reverse_char(s, word_start, i)
			word_start = i+2
	reverse_char(s, word_start, len(s)-1)
	return s



def reverse_char(s, start, end):
	
	while start<end:
		swap(s, start, end)
		start += 1
		end -= 1

	

def swap(l, start, end):
	# l = s.split()
	temp = l[start]
	l[start] = l[end]
	l[end] = temp
	# ''.join([i for i in l])

print(reverse_word("what is your name"))