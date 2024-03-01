'''
<문제분석>
board : m x n
M : 드러나지 않은 지뢰
E : 드러나지 않은 비어있는 사각형
B : 주변(8방향)에 지뢰가 없는 드러난 사각형
1부터 8 : 8개의 방향에 지뢰가 있는 개수
X : 드러난 지뢰
클릭 => M or E
- M 클릭 : X로 바뀌고 게임 오버
- E 클릭 :
 - 근처에 지뢰가 없으면, B로 바꾸고 주변 8개 방향을 다 클릭
 - 근처에 지뢰가 있으면, 그 개수(1~8)로 바꾸고 스탑 

<제한사항>
m = 행의 길이
n = 열의 길이
1 <= m, n <= 50
m과 n이 기존에 사용하던 열과 행이 아니네?

<아이디어>
BFS로 B인 친구들 다 큐에 담으면 되겠다!

'''

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        N, M = len(board), len(board[0])
        r, c = click
        print(N, M, r, c)
        dr, dc = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
        visited = [[0] * M for _ in range(N)]

        def is_in_range(r, c):
            return 0 <= r < N and 0 <= c < M

        def count_mine(r, c):
            mine_cnt = 0
            for i in range(8):
                n_r, n_c = r + dr[i], c + dc[i]
                if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
                    if board[n_r][n_c] == "M":
                        mine_cnt += 1
            return mine_cnt

        def bfs(r, c):
            visited[r][c] = 1
            dq = deque()
            dq.append((r, c))

            while dq:
                c_r, c_c = dq.popleft()
                for i in range(8):
                    n_r, n_c = c_r + dr[i], c_c + dc[i]
                    if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
                        mine_cnt = count_mine(n_r, n_c)
                        if mine_cnt == 0:
                            dq.append((n_r, n_c))
                            visited[n_r][n_c] = 1
                            board[n_r][n_c] = "B"
                        else:
                            visited[n_r][n_c] = 1
                            board[n_r][n_c] = str(mine_cnt)

        if board[r][c] == "M":
            board[r][c] = "X"
        else:
            mine_cnt = count_mine(r, c)
            if mine_cnt == 0:
                board[r][c] = "B"
                bfs(r, c)
            else:
                board[r][c] = str(mine_cnt)

        return board