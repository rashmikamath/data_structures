def fibonacci_recur(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fibonacci_recur(n-1)+fibonacci_recur(n-2)

def fibonacci_recur_memo(n, memo):
	if n == 1 or n==2:
		return 1
	if n in memo.keys():
		memo.get(n)
	res =  fibonacci_recur_memo(n-1, memo)+fibonacci_recur_memo(n-2, memo)
	memo[n] = res
	return res

def fibonacci_tabulation(n):
	n_minus_1 = 1
	n_minus_2 = 1
	nth = 1
	for i in range(3, n+1):
		nth = n_minus_1+n_minus_2
		n_minus_2 = n_minus_1
		n_minus_1 = nth
	return nth
print(fibonacci_recur(8))
print(fibonacci_recur_memo(8, dict()))
print(fibonacci_tabulation(8))