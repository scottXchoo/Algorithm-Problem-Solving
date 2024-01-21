from collections import deque

def solution(places):
    n = len(places)
    
    def is_in_range(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def dist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def bfs(x, y, arr):
        visited = [[False] * n for _ in range(n)]
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        q = deque()
        q.append([x, y, 0])
        visited[x][y] = True
        
        while q:
            c_x, c_y, c_cnt = q.popleft()
            print("현재 상태", c_x, c_y, c_cnt)
            if c_cnt > 2:
                break
            for i in range(4):
                n_x, n_y = c_x + dx[i], c_y + dy[i]
                if is_in_range(n_x, n_y) and not visited[n_x][n_y]:
                    print("다음 상태", n_x, n_y, arr[n_x][n_y])
                    if arr[n_x][n_y] == "P":
                        if c_cnt + 1 == 1:
                            return 0
                        elif c_cnt + 1 == 2:
                            if arr[c_x][c_y] != "X":
                                return 0
                    else:
                        q.append([n_x, n_y, c_cnt+1])
                        visited[n_x][n_y] = True
        return 1
    
    def search(place):
        arr, pos = [], []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(place[i][j])
                if place[i][j] == "P":
                    pos.append([i, j])
            arr.append(temp)
        # print("arr", arr)
        # print("pos", pos) # x와 y가 계속해서 커지는 방향으로 탐색하게끔
        ans = 0
        for i in range(len(pos)):
            x, y = pos[i]
            cnt = bfs(x, y, arr)
            print()
            print("---bfs 콜---", cnt)
            ans += cnt
        if len(pos) == ans:
            return 1
        else:
            return 0
        print("ans", ans)
        print("끝")

    answer = []
    for place in places:
        answer.append(search(place))
    return answer