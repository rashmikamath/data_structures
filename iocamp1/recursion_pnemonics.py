mnemonic_dict = {1:[],
			2:["a","b","c"],
			3:["d","e","f"],
			4:["g","h","i"],
			5:["j","k","l"],
			6:["m","n","o"],
			7:["p","q","r","s"],
			8:["t","u","v"],
			9:["w","x","y","z"],
			0:[0]}
def phone_number_mnemonics(arr, buffers, bufferIndex, nextIndex):
	if (bufferIndex >= len(buffers)) or (nextIndex >= len(arr)):
		print(buffers)
		return

	letters = mnemonic_dict.get(arr[nextIndex])

	if len(letters) == 0:
		phone_number_mnemonics(arr, buffers, bufferIndex, nextIndex+1)

	for letter in letters:
		buffers[bufferIndex] = letter
		phone_number_mnemonics(arr, buffers, bufferIndex+1, nextIndex+1)

if __name__ == "__main__":
	buffers = [0]*3
	phone_number_mnemonics([2,3,4], buffers, 0, 0)