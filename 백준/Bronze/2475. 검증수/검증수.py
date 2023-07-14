user_input = list(map(int, input().split()))
answer = 0

for i in user_input:
	answer += i**2
print(answer % 10)