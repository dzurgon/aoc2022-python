
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

		#part one
		score1 += me + 1
		if me == opponent: score1 += 3
		elif (me-1)%3 == opponent: score1 += 6
		else: score1 += 0

		#part two
		score2 += me * 3
		if me == 0:
			score2 += ((opponent - 1) % 3) + 1
		if me == 1:
			score2 += (opponent) + 1
		if me == 2:
			score2 += ((opponent + 1) % 3) + 1
	
	print("Part 1", score1)
	print("Part 2", score2)
			
