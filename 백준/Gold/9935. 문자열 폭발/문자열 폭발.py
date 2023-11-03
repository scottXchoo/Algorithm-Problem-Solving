import sys
input = sys.stdin.readline

# 입력값 처리
S = input().rstrip()
B = input().rstrip()
b = len(B)
stack = []

# 문자열 폭발 탐색
for c in S:
  stack.append(c)
  if ''.join(stack[-b:]) == B:
    for _ in range(b):
      stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')