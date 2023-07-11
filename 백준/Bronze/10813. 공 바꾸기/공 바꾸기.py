N, M = map(int, input().split(" "))
box = [str(i+1) for i in range(N)]

for _ in range(M):
	i, j = map(int, input().split(" "))
	box[i-1], box[j-1] = box[j-1], box[i-1]

print(" ".join(box))