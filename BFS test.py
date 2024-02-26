plain = [


["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["p","","","","","","","","","","","","","","","","","","","d"],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],
["","","","","","","","","","","","","","","","","","","",""],

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

#visited = set()
def dfs(start,dict,visited):
	if visited == None:
		visited = set()
	if start not in visited:
		item = plain[start[1]][start[0]]
		if item != "B":
			visited.add(start)
			for adj in dict[start]:
				dfs(adj,dict,visited)
	return visited


visited = dfs((0,5),plain_adjacency_dict,None)

print(visited)
if (19,5) in visited:
	pass
	print('PATH FOUND')
else:
	pass
	print("NO PATH FOUND")
		
	







	





		



