class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def box_nums(num, erase):
            row_start = ((num - 1) // 3) * 3
            col_start = ((num - 1) % 3) * 3

            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] != ".":
                        erase.append(int(board[i][j]))

        def box_position(i, j):
            return (i // 3) * 3 + (j // 3) + 1

        def erase_nums(i, j):
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            erase = []

            # 행 조건
            arr = board[i]
            for k in range(9):
                if arr[k] != ".":
                    erase.append(int(arr[k]))

            # 열 조건
            for k in range(9):
                if board[k][j] != ".":
                    erase.append(int(board[k][j]))

            # 박스 조건
            box_num = box_position(i, j)
            box_nums(box_num, erase)

            renums = [x for x in nums if x not in erase]
            return renums

        def backtrack(depth):
            if depth == len(blanks): # 모든 빈 칸을 채웠을 때
                return True

            i, j = blanks[depth]
            renums = erase_nums(i, j)
            
            for num in renums:
                board[i][j] = str(num)
                if backtrack(depth+1): # 유효한 해를 찾았을 때
                    return True
                board[i][j] = "." # 해를 찾지 못했으면 원래 상태로 되돌림
                
            return False # 이 위치에서는 해를 찾지 못함
        
        blanks = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    blanks.append([i, j])

        backtrack(0)
        