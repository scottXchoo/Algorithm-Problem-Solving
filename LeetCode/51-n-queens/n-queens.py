class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        board = [["."] * n for _ in range(n)]

        def is_valid(row, col):
            # row는 고정이니까 col만 체크하기
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # 왼쪽 상단부터 차곡차곡 퀸을 둘 예정이니까 45도와 135도만 체크하기
            ## 45도 체크
            r, c = row - 1, col - 1
            while 0 <= r and 0 <= c:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1
            ## 135도 체크
            r, c = row - 1, col + 1
            while c < n and 0 <= r:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        def backtracking(row):
            if row == n:
                answer.append(["".join(row) for row in board])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtracking(row + 1)
                    board[row][col] = "."

        backtracking(0)
        return answer