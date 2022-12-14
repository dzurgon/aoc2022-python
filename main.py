def day1():
	input = open("d1.txt", "r").read().split("\n")
	lis = [0] * (input.count("\n")+1)
	index = 0
	for i in input:
		if i != "\n": 
			lis[index] += int(i)
		else: index += 1
	lis.sort(reverse=True)
	print("Sum of greatest:", lis[0])
	print("Sum of three greatest:", (lis[0]+lis[1]+lis[2]))
def day2():
	input = open("d2.txt", "r").read().split("\n")
	score1 = 0
	score2 = 0
	for i in input:
		#setup
		opponent = ord(i[0]) - 65
		me = ord(i[2]) - 88
		print(opponent, me)
		#part one
		score1 += me + 1
		if me == opponent: score1 += 3
		elif (me-1)%3 == opponent: score1 += 6
		else: score1 += 0
		#part two
		score2 += me * 3
		if me == 0:	score2 += ((opponent - 1) % 3) + 1
		if me == 1:	score2 += (opponent) + 1
		if me == 2:	score2 += ((opponent + 1) % 3) + 1
	print("Part 1", score1)
	print("Part 2", score2)
def day3():
	#part one
	score = 0
	input = open("d3.txt", "r").read().split("\n")
	for i in input:
		comp1 = i[0:(len(i)//2)]
		comp2 = i[len(i)//2:]
		for q in comp1:
			if q in comp2 and q.islower():
					score += ord(q) - 96
					break
			elif q in comp2 and q.isupper():
					score += ord(q) - 38
					break
			else:
				score += 0

	#part two
	score2 = 0
	for i in range(0, len(input), 3):
		for q in input[i]:
			if q in input[i+1] and q in input[i+2]:
				if q.islower():
					score2 += ord(q) - 96
					break
				elif q.isupper():
					score2 += ord(q) - 38
					break
		
	print("Part 1", score)
	print("Part 2", score2)
def day4():
	i = [int(q) for q in open("d4.txt", "r").read().replace('-','\n').replace(',','\n').split()]

	#part 1
	score = 0
	for q in range(0,len(i),4):
		if (i[q] >= i[q+2] and i[q+3] >= i[q+1]) or (i[q+2] >= i[q] and i[q+1] >= i[q+3]):
			score += 1
			
	#part 2
	score2 = 0
	score3 = 0
	for q in range(0, len(i), 4):
		if not (i[q+2] > i[q+1] or i[q] > i[q+3]):
			score2 += 1
		else: 
			print(i[q:q+4])
			score3 += 1

	print("Part 1", score)
	print("Part 2", score2)
def day5():
	# Get input and configure stack/moves
	input = open("d5.txt", "r").read().split("\n")
	stack = input[:8]
	moves = [i.replace("move","").replace("from","").replace("to","").split() for i in input[10:]]
	
	arr = []
	for i in range(1, len(stack[0]), 4):
		arr.append([])
		for q in range(len(stack), 0, -1):
			if stack[q-1][i] != " ":
				arr[i//4].append(stack[q-1][i])

	
	# Part 1
	for i in moves:
		_amount = int(i[0])
		_from = int(i[1])-1
		_to = int(i[2])-1
	
		for q in range(_amount):
			arr[_to].append(arr[_from].pop())

	# Part 1 printout
	for i in range(len(arr)):
		print(arr[i][-1], end ="")
	print()
	# End of part 1 printout

	# Initialize arr2
	arr2 = []
	for i in range(1, len(stack[0]), 4):
		arr2.append([])
		for q in range(len(stack), 0, -1):
			if stack[q-1][i] != " ":
				arr2[i//4].append(stack[q-1][i])

	# Part 2	
	for i in moves:
		_amount = int(i[0])
		_from = int(i[1])-1
		_to = int(i[2])-1
		from_len = len(arr2[_from])

		for q in range(from_len - _amount, from_len):
			arr2[_to].append(arr2[_from][q])
			
		for q in range(_amount):
			arr2[_from].pop(-1)

	for i in range(len(arr2)):
		print(arr2[i][-1], end ="")
	print()	
