N = int(input())
S = input().strip()
stack = []
counter = [0] * N

for idx in range(N):
  if S[idx] == '(':
    stack.append(idx)
  else:
    if stack:
      counter[idx] = counter[stack[-1]] = 1
      stack.pop()

ans = 0
cnt = 0
for num in counter:
  if num == 1:
    cnt += 1
    ans = max(ans, cnt)
  else:
    cnt = 0

print(ans)