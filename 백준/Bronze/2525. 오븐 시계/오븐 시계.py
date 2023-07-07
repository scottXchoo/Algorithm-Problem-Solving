H, M = map(int, input().split())
timer = int(input())

H += timer // 60
M += timer % 60

if M >= 60:
		H += 1
		M -= 60
if H >= 24:
		H -= 24

print(H, M)