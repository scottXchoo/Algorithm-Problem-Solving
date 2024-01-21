import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    routes = []
    maps = [["."] * m for _ in range(n)]
    
    def dist_num(x, y):
        return abs(x - r + 1) + abs(y - c + 1)
    
    def router(routes):
        answer  = ''
        for r in routes:
            if r == 0:
                answer += 'd'
            elif r == 1:
                answer += 'l'
            elif r == 2:
                answer += 'r'
            elif r == 3:
                answer += 'u'
        return answer
    
    def is_in_range(x, y):
        return 0 <= x < n and 0 <= y < m
    
    def dfs(depth, x, y):
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        
        if k - depth < dist_num(x, y):
            return True
        elif depth == k:
            if (x == r-1 and y == c-1) and (k - depth) % 2 == 0:
                return False
            else:
                return True
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_in_range(nx, ny):
                routes.append(i)
                if dfs(depth+1, nx, ny):
                    routes.pop()
                else:
                    return False
        return True
    
    dist = dist_num(x-1, y-1)
    if dist > k or (k - dist) % 2 == 1: # 이동 거리보다 k가 작으면, 애초에 못 감
        return "impossible"
    
    if dfs(0, x-1, y-1):
        return "impossible"
    else:
        answer = router(routes)
        return answer