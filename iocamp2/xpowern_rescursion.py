def postive_power(x, n):
	#check if power is zero
	if n==0:
		return 1
	#check if power is 1
	if n == 1:
		return x

	halfpower = postive_power(x, n/2)
	if n%2==0:
		return halfpower*halfpower
	else:
		return halfpower*halfpower*x

def find_power(x, n):
	if x==0 and n<=0:
		raise NotImplementedError("issue")
	result = postive_power(abs(x), abs(n))
	if n<0:
		result = 1/result
	if x<0 and n%2!=0:
		result = -1*result
	return result

print(postive_power(-2, 3))
print(postive_power(2, -3))