numbers = range(1,10)
positions = []
chuncks = {}
board = {}

def getp(a,b):
	return int(f"{a}{b}")

def chunck(position):
	return [k for k,v in chuncks.items() if v == chuncks[position]]

def getposx(position):
	return int(str(position)[0])

def getposy(position):
	return int(str(position)[1])


x=1
y=1

for i in numbers:
	for j in numbers:
		positions.append(getp(j,i))
		chuncks[getp(j,i)] = getp(x,y)
		if ((j>2) and (j%3 == 0)):
			x+=1
	x=1
	if ((i>2) and (i%3 == 0)):
		y+=1

# board[11]=1
# board[21]=2
# board[31]=3
# board[12]=4
# board[22]=5
# board[32]=6
# board[13]=7
# board[23]=8
# board[33]=9
# position = 12
# number=4
# duplicate = False
# print( chunck(position))


# for posxy in chunck(position):
# 	print(posxy)
# 	print(board[posxy] == number)
# 	try:
# 		if board[posxy] == number:
# 			duplicate = True
			
# 	except:
# 		pass

# print(duplicate)

# lst = chunck(12)
# print(board[11])
# print(number)
# print(board[11] == number)
# print(lst)

for position in positions:
	print(position)
	if not position in board.keys():
		print(position)
		for number in numbers:
			duplicate=False
			for posx in numbers:
				try:
					if board[getp(posx, getposy(position))] == number:
						duplicate=True
				except:
					pass
			for posy in numbers:
				try:
					if board[getp(getposx(position), posy)] == number:
						duplicate=True
				except:
					pass

			for posxy in chunck(position):
				try:
					if board[posxy] == number:
						duplicate = True
				except:
					pass
			
			if duplicate == False:
				board[position] = number
				print(position ,":",number)
				break
			

print("Board: ")

boardstr=""
for key in board.keys():
	boardstr += "|"+str(board[key])
	if key in range(91,100):
		boardstr += "\n-------------------\n"

print(boardstr)





	