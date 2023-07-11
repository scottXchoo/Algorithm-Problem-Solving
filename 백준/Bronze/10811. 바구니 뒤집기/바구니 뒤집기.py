N, M = map(int, input().split())
basket = [str(i) for i in range(1, N+1)]

for _ in range(M):
	i,j = map(int, input().split())
	temp = basket[i-1:j]
	temp.reverse()
	basket[i-1:j] = temp

print(" ".join(basket))