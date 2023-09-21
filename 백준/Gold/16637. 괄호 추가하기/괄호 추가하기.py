import sys

n = int(input())
s = input()
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
  if idx == n - 1:
    res = max(res, value)
    return
	# 괄호 X
  if idx + 2 < n:
    dfs(idx + 2, calc(value, s[idx + 1], int(s[idx + 2])))
  # 괄호 O
  if idx + 4 < n:
    dfs(idx + 4, calc(value, s[idx + 1], calc(int(s[idx + 2]), s[idx + 3], int(s[idx + 4]))))

dfs(0, int(s[0]))
print(res)