'''
<문제분석>
(x, y) => (r, c)
미로 탈출 조건
1. 격자 바깥 X
2. (x, y)에서 (r, c)까지 이동하는 거리가 총 k (두 번 이상 방문 괜찮)
3. 미로에서 탈출한 경로를 문자열로 나타냈을 때, 문자열이 사전 순으로 가장 빠른 경로로 탈출
d: 아래쪽, l: 왼쪽, r: 오른쪽, u: 위쪽

<제한사항>
2 <= n, m <= 50
(x, y) != (r, c)
1 <= k <= 2500

<아이디어>
dlru 순서로 ddddd부터 하나씩 맞는지 체크
아니면, 다시 뒤로 빽(백트래킹)
미로를 탈출할 수 없으면, "impossible"

- 남은 거리(dist?) > 갈 수 있는 거리(k - dist)
- [k - dist]가 홀수면, 애초에 못 감 (도착한 뒤, 왔다갔다 - 짝수)

maps를 따로 만든다.
index에서 바로바로 path를 갖고 있으면 될 듯?
'''
import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
    direction = ['d', 'l', 'r', 'u']
    distance = abs(x - r) + abs(y - c)
    if (distance > k) or (k - distance) % 2 == 1:
        return "impossible"
    
    def dfs(c_x, c_y, d):
        if (d == k) and (c_x == r) and (c_y == c):
            return True
        elif not (0 < c_x <= n and 0 < c_y <= m):
            return False
        elif (abs(c_x - r) + abs(c_y - c)) > (k - d):
            return False
        
        for i in range(4):
            n_x, n_y = c_x + dx[i], c_y + dy[i]
            route.append(direction[i])
            if dfs(n_x, n_y, d+1):
                return True
            else:
                route.pop()
        return False
    
    route = []
    if dfs(x, y, 0):
        return "".join(route)
    else:
        return "impossible"