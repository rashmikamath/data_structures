def merge_sort(arr, low, high):
	mid = low+(high-low)//2
	merge_sort(arr, low, mid)
	merge_sort(arr, mid+1, high)
	merge(arr, mid, low, high)

def merge(arr, mid, low, high):
	res = [-1]*(high-low+1)
	rp = 0
	i = low
	j = mid+1
	while i <= mid and j<=high:
		if arr[i] <= arr[j]:
			res[rp] = arr[i]
			rp += 1
			i += 1
		else:
			res[rp] = arr[j]
			rp += 1
			j += 1
	while i<=mid:
		res[rp] = arr[i]
		i += 1
		rp += 1
	while j <=high:
		res[rp] = arr[j]
		j += 1
		rp += 1
	for i in range(len(res)):
		arr[start+k] = res[k]
		
