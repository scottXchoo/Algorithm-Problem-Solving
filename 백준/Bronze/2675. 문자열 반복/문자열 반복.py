T = int(input())

for i in range(T):
	R, S = input().split()
	R = int(R)
	S = str(S)
	for x in range(len(S)):
		print(R*S[x], end="")
	print() # 줄넘김