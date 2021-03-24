def find_set_unique_char(s):
	right = 0
	left = 0
	s_dict = {}
	s_dict[s[0]] = 0
	longest = 1
	while right < len(s)-1:
		right += 1
		toAdd = s[right]
		if toAdd in s_dict and s_dict[toAdd] >= left:
			left = s_dict[toAdd]+1
		s_dict[toAdd] = right
		current_len = right-left+1

		if current_len > longest:
			longest = current_len
			result = [right, left]
	return result

print(find_set_unique_char("whatwhywhere"))