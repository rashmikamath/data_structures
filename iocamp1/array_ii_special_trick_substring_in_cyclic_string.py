def substring(s, sb):
	if len(s)==0 or s==None:
		return 
	return sb in (s+s)

print(substring("bobcat", "atbob"))