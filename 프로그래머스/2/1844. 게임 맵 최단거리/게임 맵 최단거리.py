from collections import deque

def solution(maps):
    # 0: 벽 O, 1: 벽 X
    # queue에 초깃값 넣고
    # pop으로 현재 위치 빼고
    # 다음 위치: 현재 위치 + 동서남북
    # 종료 조건: 도달했는가 안 했는가 => 움직인 횟수 return
    # 만약 갈 곳 없으면 Out => -1 return
    # 벽이 있거나 밖이면 continue
    # 그게 아니면, queue에 넣기
    q = deque([])
    n = len(maps) # 세로 맞지?
    m = len(maps[0]) # 가로 맞지?
    
    delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[0] * m for _ in range(n)]
    
    q.append((0, 0, 1))
    visited[0][0] = 1
    
    while q:
        x, y, cnt = q.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = 1
        
    return -1


