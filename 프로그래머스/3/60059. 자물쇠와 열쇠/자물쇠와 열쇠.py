def solution(key, lock):
    n, m = len(lock), len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    def rotate(key): # 90도 시계방향 회전
        n = len(key)
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                result[j][n-i-1] = key[i][j]
        return result
    
    def check(lock): # lock이 모두 1로 채워졌는지 확인
        n = len(lock) // 3
        for i in range(n, n*2):
            for j in range(n, n*2):
                if lock[i][j] != 1:
                    return False
        return True
    
    for rotation in range(4):
        key = rotate(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[i+x][j+y] += key[i][j]
                if check(new_lock):
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i+x][j+y] -= key[i][j]
    return False