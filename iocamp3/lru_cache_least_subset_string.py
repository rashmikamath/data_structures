def shortest_substring(doc, s):
	map_dict = dict()
	ll = LinkedList()
	for index, word in enumerate(doc):
		if word not in s:
			continue

			if word in map_dict.keys():
				todelete = map_dict.get(word)
				ll.delete(todelete)
			

		new_node = Node(word, index)
		map_dict[word] = index
		ll.append(new_node)

		if len(map_dict)== len(s):
			start = ll.head.index
			end = ll.tail.index+len(ll.tail.word)-1
			if res == None or end-start+1< len(res):
				res = doc[start:end+1]