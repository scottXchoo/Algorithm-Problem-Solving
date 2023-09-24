import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def fbfs():
    while fq:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if maze[nx][ny] == "#" or fire[nx][ny]:
                continue
            fire[nx][ny] = fire[x][y] + 1
            fq.append((nx, ny))

def hbfs():
    while hq:
        x, y = hq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < R and 0 <= ny < C):
                print(human[x][y])
                return
            if maze[nx][ny] == "#" or human[nx][ny]:
                continue
            ## human의 현재 위치보다 한 칸 앞선 시간에 불이 이미 갔거나 동시에 갈 때 && fire[nx][ny]가 0일 때는 X (= and fire[nx][ny]
            if human[x][y] + 1 >= fire[nx][ny] and fire[nx][ny]:
                continue
            hq.append((nx, ny))
            human[nx][ny] = human[x][y] + 1
    print("IMPOSSIBLE")
    return

# main
R, C = map(int, input().split())
maze = []
hq = deque()
fq = deque()
## 방문 처리 && 걸린 시간
human = [[0] * C for _ in range(R)]
fire = [[0] * C for _ in range(R)]
for i in range(R):
    maze.append(list(input().strip()))
    for j in range(C):
        if maze[i][j] == "F":
            fq.append((i, j))
            fire[i][j] = 1
        elif maze[i][j] == "J":
            hq.append((i, j))
            human[i][j] = 1

fbfs()
hbfs()
