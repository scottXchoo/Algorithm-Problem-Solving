numbers = []

for _ in range(9):
		i = int(input())
		numbers.append(i)

print(max(numbers))
print(numbers.index(max(numbers)) + 1)