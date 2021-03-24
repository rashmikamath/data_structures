mnemonics_dict = {
	0:[],
	1:[],
	2:["a","b","c"],
	3:["d","e","f"],
	4:["g","h","i"],
	5:["j","k","l"],
	6:["m","n","o"],
	7:["p","q","r","s"],
	8:["t","u","v"],
	9:["w","x","y","z"],
}
def mnemonics(arr, buff, next_index, buff_index):
	#termination case 
	if buff_index==len(buff) or next_index==len(arr):
		print(buff[:buff_index])
		return 

	letter = mnemonics_dict[arr[next_index]]

	#check if the list is empty
	if len(letter)==0:
		mnemonics(arr, buff, next_index+1, buff_index)

	#find the candidate to place in buffer
	for l in letter:
		buff[buff_index] = l
		mnemonics(arr, buff, next_index+1, buff_index+1)

mnemonics([0,2,3],[0,0,0],0,0)
print("=====new_set====")
mnemonics([4,5,7],[0,0,0], 0, 0)