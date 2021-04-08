map_dict = {0:[],
			1:[],
			2:["a","b","c"],
			3:["d","e","f"],
			4:["g", "h", "i"],
			5:["j", "k","l"],
			6:["m", "n", "o"],
			7:["p","q","r","s"],
			8:["t", "u", "v"],
			9:["w", "x", "y", "z"]
			}
def phone_number(arr):
	if len(arr)==0 or arr==None:
		return 
	buff = [0]*len(arr)
	phone_number_helper(arr, buff, 0, 0)

def phone_number_helper(arr, buff, next_index, buff_index):
	#termination case
	if buff_index==len(buff) or next_index==len(arr):
		print(buff[:buff_index])
		return

	#find the candidates to place
	ch = map_dict.get(arr[next_index])

	#handle the case of 0 and 1
	if len(ch) == 0:
		phone_number_helper(arr, buff, next_index+1, buff_index)

	#place the candidate
	for c in ch:
		buff[buff_index] = c
		phone_number_helper(arr, buff, next_index+1, buff_index+1)

phone_number([4,5,2])