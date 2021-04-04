def max_trade_stock_price(a):
	max_trade = 0
	min_so_far = float("inf")
	for i in range(len(a)):
		min_so_far = min(a[i], min_so_far)
		max_i = a[i]-min_so_far
		if max_i > max_trade:
			max_trade = max_i
	return max_trade

print(max_trade_stock_price([2,3,1,4,5,7,5,4]))