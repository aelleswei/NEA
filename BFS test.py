plain = [


["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["p","","","","","","","","","","","","","","","","","","","d"],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],
["","","","","B","","","","","","","","","","","","","","",""],

]

def adjacent_nodes(node):

	def check_tile(current,hor,ver):
			current = current
			tile_check = (current[0] + hor, current[1] + ver)
			return tile_check

	def check_around(current):
		current = current
		array = []
		tile0 = check_tile(current,-1,0)
		if valid_tile(tile0):
			array.append(tile0)
		
		tile1 = check_tile(current,-1,1)
		if valid_tile(tile1) == True:
			array.append(tile1)
		
		tile2 = check_tile(current,-1,-1)
		if valid_tile(tile2) == True:
			array.append(tile2)
		
		tile3 = check_tile(current,0,1)
		if valid_tile(tile3) == True:
			array.append(tile3)
		
		tile4 = check_tile(current,0,-1)
		if valid_tile(tile4) == True:
			array.append(tile4)
		
		tile5 = check_tile(current,1,0)
		if valid_tile(tile5) == True:
			array.append(tile5)
		
		tile6 = check_tile(current,1,1)
		if valid_tile(tile6) == True:
			array.append(tile6)
		
		tile7 = check_tile(current,1,-1)
		if valid_tile(tile7) == True:
			array.append(tile7)

		return array

	def valid_tile(tile):
		if tile[0] > 19 or tile[0] < 0 or tile[1] > 11 or tile[1] < 0:
			valid = False
		else:
			valid = True

		return valid


	adjacent = check_around(node)
	return adjacent

plain_adjacency_dict = {}
for i in range(len(plain)):
	for j in range(len(plain[i])):
		plain_adjacency_dict[(j,i)] = adjacent_nodes((j,i))


def bfs(start,end):
	queue = []
	visited = []
	queue.append(start)
	visited.append(start)

	while len(queue) > 0:
		head = queue.pop(0)
		if plain[head[1]][head[0]] != "B":
			for neighbour in plain_adjacency_dict[head]:
				if plain[neighbour[1]][neighbour[0]] != 'B':
					queue.append(neighbour)
		visited.append(head)
	print(visited)
	if end in visited:
		print('PATH')
	else:
		print('NO PATH')
		

		

bfs((0,5),(19,5))






	





		



