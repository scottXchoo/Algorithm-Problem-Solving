from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
dp = [0] * (MAX + 1)
dq = deque()
dq.append(N)
answer = 0

while True:
    cx = dq.popleft()
    if cx == K:
        answer = dp[cx]
        break

    for nx in [cx + 1, cx - 1, 2 * cx]:
        if 0 <= nx <= MAX:
            if dp[nx] == 0:
                dp[nx] = dp[cx] + 1
                dq.append(nx)

print(answer)