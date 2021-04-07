def print_spiral(arr):
	if len(arr)==0 or arr==None 

	for i in range(len(arr)//2):
		print_layer(arr, 0, len(arr)-1-layer, len(arr)-1-layer)

def print_layer(arr, layer, lastrow, lastcol):
	if lastcol==layer and lastrow==layer:
		print(arr[layer][layer])

	for i in range(layer, lastcol):
		print(arr[layer][i])

	for i in range(layer, lastrow):
		print(arr[i][lastcol])

	for i in range(lastcol, layer):
		print(arr[lastrow][i])

	for i in range(lastrow, layer):
		print(arr[i][layer])