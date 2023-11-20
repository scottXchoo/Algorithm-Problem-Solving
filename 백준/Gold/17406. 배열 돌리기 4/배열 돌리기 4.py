import sys

N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
operation = [list(map(int, input().split())) for _ in range(K)]

min_ans = sys.maxsize
visited = [-1] * K

def rotation(matrix, r, c, s): # 회전 연산 함수
  for i in range(s):
    # 가장 왼쪽 윗칸 : r1, c1 & 가장 오른쪽 아랫칸 r2, c2
    r1, c1, r2, c2 = r-s+i, c-s+i, r+s-i, c+s-i
    temp = matrix[r1][c1] # 가장 왼쪽 윗칸 저장
    # c1열
    for idx in range(r1, r2):
      matrix[idx][c1] = matrix[idx+1][c1]
    # r2행
    for idx in range(c1, c2):
      matrix[r2][idx] = matrix[r2][idx+1]
    # c2열
    for idx in range(r2, r1, -1):
      matrix[idx][c2] = matrix[idx-1][c2]
    # r1행
    for idx in range(c2, c1+1, -1):
      matrix[r1][idx] = matrix[r1][idx-1]
    matrix[r1][c1+1] = temp # 저장한 가장 왼쪽 윗칸 값을 바로 다음 열에 넣기
  return matrix

def dfs(L, cur):
  global min_ans
  if L == K:
    opelist = [operation[idx] for idx in visited]
    copy_matrix = [m[:] for m in matrix]
    for r, c, s in opelist:
      copy_matrix = rotation(copy_matrix, r-1, c-1, s)
    min_ans = min(min_ans, min([sum(temp) for temp in copy_matrix]))
    return
  for i in range(K):
    if visited[i] == -1:
      visited[i] = cur
      dfs(L + 1, cur + 1)
      visited[i] = -1

dfs(0, 0)
print(min_ans)