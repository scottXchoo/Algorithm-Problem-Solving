from collections import deque

def get_next_pos(pos, board):
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    (r1, c1), (r2, c2) = pos
    next_pos_list = []
    
    # 동남서북 이동
    for i in range(4):
        next_r1, next_c1 = (r1 + dr[i], c1 + dc[i])
        next_r2, next_c2 = (r2 + dr[i], c2 + dc[i])
        if board[next_r1][next_c1] == 0 and board[next_r2][next_c2] == 0:
            next_pos_list.append(((next_r1, next_c1), (next_r2, next_c2)))
            
    # 가로일 때, 회전
    if r1 == r2:
        # 위쪽이 비었을 때, 회전 (위로 회전)
        if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:
            next_pos_list.append(((r2 - 1, c2), (r2, c2)))
            next_pos_list.append(((r1, c1), (r1 - 1, c1)))
        # 아래쪽이 비었을 때, 회전 (아래로 회전)
        if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
            next_pos_list.append(((r1, c1), (r1 + 1, c1)))
            next_pos_list.append(((r2, c2), (r2 + 1, c2)))
            
    # 세로일 때, 회전
    if c1 == c2:
        # 오른쪽이 비었을 때, 회전 (오른쪽으로 회전)
        if board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:
            next_pos_list.append(((r1, c1), (r1, c1 + 1)))
            next_pos_list.append(((r2, c2), (r2, c2 + 1)))
        # 왼쪽이 비었을 때, 회전 (왼쪽으로 회전)
        if board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
            next_pos_list.append(((r1, c1), (r1, c1 - 1)))
            next_pos_list.append(((r2, c2), (r2, c2 - 1)))
    
    return next_pos_list

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for r in range(n):
        for c in range(n):
            new_board[r + 1][c + 1] = board[r][c]

    start_pos = ((1, 1), (1, 2))
    start_dist = 0
    q = deque()
    q.append((start_pos, start_dist))
    
    visited = set()
    visited.add(start_pos)

    while q:
        cur_pos, cur_dist = q.popleft()
        
        if (n, n) in cur_pos:
            return cur_dist
        
        for next_pos in get_next_pos(cur_pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cur_dist + 1))
                visited.add(next_pos)