num = []

for _ in range(10):
	a = int(input())
	num.append(a % 42)

print(len(set(num)))