n = int(input())

for _ in range(n):
	ox_list = list(input())
	score = 0
	sum_score = 0
	for ox in ox_list:
		if ox == "O":
			score += 1
			sum_score += score
		else:
			score = 0
	print(sum_score)