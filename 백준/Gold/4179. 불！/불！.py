import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def fbfs():
    while fq:
        r, c = fq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if maze[nr][nc] == "#" or fire[nr][nc]:
                continue
            fire[nr][nc] = fire[r][c] + 1
            fq.append((nr, nc))

def hbfs():
    while hq:
        r, c = hq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                print(human[r][c])
                return
            if human[nr][nc] or maze[nr][nc] == "#":
                continue
            if fire[nr][nc] and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            hq.append((nr, nc))
    print("IMPOSSIBLE")
    return

# main
R, C = map(int, input().split())
maze = []
hq = deque()
fq = deque()
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "J":
            hq.append((i, j))
            human[i][j] = 1
        elif maze[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1
fbfs()
hbfs()