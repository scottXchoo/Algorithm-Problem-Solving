import sys
N = int(input())
S = input()
res = -1 * sys.maxsize

def calc(num1, oper, num2):
  if oper == '+':
    return num1 + num2
  if oper == '-':
    return num1 - num2
  if oper == '*':
    return num1 * num2

def dfs(idx, value):
  global res

  # 계산 끝! 계속해서 최댓값 업데이트
  if idx == N - 1:
    res = max(res, value)
    return
  # 괄호 X
  if idx + 2 < N:
    dfs(idx + 2, calc(value, S[idx + 1], int(S[idx + 2])))
  # 괄호 O
  if idx + 4 < N:
    next_calc = calc(int(S[idx + 2]), S[idx + 3], int(S[idx + 4]))
    dfs(idx + 4, calc(value, S[idx + 1], next_calc))

dfs(0, int(S[0]))
print(res)
