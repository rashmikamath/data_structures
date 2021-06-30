def min_move_func(n, cache):
	if n in cache.keys():
		return cache[n]
	if n==0:
		return 0
	if n==1:
		return 1
	if n==2:
		return 2
	min_moves = n
	for i in range(1, n):
		min_moves = min(min_moves, max(i, 1+min_move_func(n-i, cache)))
	cache[n] = min_moves
	return min_moves

def egg_drop(n):
	return min_move_func(n, dict())

print(egg_drop(4))
print(egg_drop(8))
print(egg_drop(20))