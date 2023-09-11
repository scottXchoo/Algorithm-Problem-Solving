import sys
import math
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, sys.stdin.readline().split())

arr = list()
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

def bfs(i, j):
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True
    union = [(i, j)]
    cnt = arr[i][j]
    
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                visited[nx][ny] = True
                dq.append((nx, ny))
                union.append((nx, ny))
                cnt += arr[nx][ny]
                
    for x, y in union:
        arr[x][y] = math.floor(cnt / len(union))
    
    return len(union)

result = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    if not flag:
        break
    result += 1
    
print(result)