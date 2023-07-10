N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
	i, j, k = map(int, input().split())
	for index in range(i, j+1):
		basket[index - 1] = k

for index in range(N):
	print(basket[index], end = ' ')