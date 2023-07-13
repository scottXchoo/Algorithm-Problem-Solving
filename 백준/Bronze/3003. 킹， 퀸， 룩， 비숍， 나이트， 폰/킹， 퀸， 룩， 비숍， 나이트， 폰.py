black_piece = [1, 1, 2, 2, 2, 8]
white_piece = list(map(int, input().split()))

for i in range(len(black_piece)):
	print(black_piece[i] - white_piece[i], end = " ")