x = list(map(int, input().split()))

if x == sorted(x):
	print("ascending")
elif x == sorted(x, reverse=True):
	print("descending")
else:
	print("mixed")