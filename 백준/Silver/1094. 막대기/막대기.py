X = int(input())
cnt = 0
N = 64

while X > 0:
	if N > X:
		N = N // 2
	else:
		cnt += 1
		X -= N

print(cnt)