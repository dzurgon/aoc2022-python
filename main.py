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