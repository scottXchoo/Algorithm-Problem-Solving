'''
<문제분석>
가장 왼쪽 상단 : (1, 1)
두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 끝
회전도 가능
- 회전하는 곳에 벽(1)이 있으면 X
return : 필요한 최소 시간!!

<제한사항>
- board의 한 변의 길이는 5 이상 100 이하
- 항상 목적지에 도착할 수 있는 board만 제공

<아이디어>
((r1, c1), (r2, c2))
상하좌우 : 원래 하던 대로 하면 될 듯?
가로일 때 (r1 == r2)
- 아래 벽 X : 아래로 회전 가능
- 위 벽 X : 위로 회전 가능
세로일 때 (c1 == c2)
- 왼쪽 벽 X : 왼쪽으로 회전 가능
- 오른쪽 벽 X : 오른쪽으로 회전 가능

"현재 위치를 인자로 받으면, 가능한 이동 및 회전을 적용한 위치를 리턴하는 함수를 만들자"
그 함수에 나온 위치를 n_r, n_c로 두고 큐에 넣으면 됨
'''

from collections import deque

def solution(board):
    answer = 0
    N = len(board)
    new_board = [[1] * (N+2) for _ in range(N+2)]
    for r in range(N):
        for c in range(N):
            new_board[r+1][c+1] = board[r][c]

    def is_in_range(r, c):
        return 1 <= r <= N and 1 <= c <= N
    
    def next_pos(r1, c1, r2, c2):
        n_p = []
        n_r1, n_c1, n_r2, n_c2 = 0, 0, 0, 0
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            n_r1, n_c1 = r1 + dr, c1 + dc
            n_r2, n_c2 = r2 + dr, c2 + dc
            if new_board[n_r1][n_c1] == 0 and new_board[n_r2][n_c2] == 0:
                n_p.append([n_r1, n_c1, n_r2, n_c2])
        
        if r1 == r2: # 가로
            if new_board[r1+1][c1] == 0 and new_board[r2+1][c2] == 0: # 아래로 회전
                n_p.append([r2, c2, r2+1, c2]) # 반시계 회전
                n_p.append([r1, c1, r1+1, c1]) # 시계 회전
            elif new_board[r1-1][c1] == 0 and new_board[r2-1][c2] == 0: # 위로 회전
                n_p.append([r1, c1, r1-1, c1]) # 반시계 회전
                n_p.append([r2, c2, r2-1, c2]) # 시계 회전
        if c1 == c2: # 세로
            if new_board[r1][c1-1] == 0 and new_board[r2][c2-1] == 0: # 왼쪽 회전
                n_p.append([r2, c2, r2, c2-1]) # 반시계 회전
                n_p.append([r1, c1, r1, c1-1]) # 시계 회전
            elif new_board[r1][c1+1] == 0 and new_board[r2][c2+1] == 0: # 오른쪽 회전
                n_p.append([r1, c1, r1, c1+1]) # 반시계 회전
                n_p.append([r2, c2, r2, c2+1]) # 시계 회전
        return n_p
                
    dq = deque()
    dq.append((1, 1, 1, 2, 0))
    
    visited = set()
    visited.add((1, 1, 1, 2))
    
    while dq:
        r1, c1, r2, c2, cnt = dq.popleft()
        
        if (r1 == N and c1 == N) or (r2 == N and c2 == N):
            answer = cnt
            break
            
        n_p = next_pos(r1, c1, r2, c2)
        for n_r1, n_c1, n_r2, n_c2 in n_p:
            if (n_r1, n_c1, n_r2, n_c2) not in visited:
                dq.append((n_r1, n_c1, n_r2, n_c2, cnt+1))
                visited.add((n_r1, n_c1, n_r2, n_c2))
        
    return answer