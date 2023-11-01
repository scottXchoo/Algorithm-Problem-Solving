N = int(input())
arr = [int(input()) for _ in range(N)]
H, CNT, ans = 0, 1, 0
stack = []

for h in arr:
  while stack and stack[-1][H] < h: # 스택이 비어있지 않고 스택의 끝 값보다 크면
    ans += stack.pop()[CNT] # 스택의 끝 값 pop & ans 추가
  if not stack: # 스택이 비어있으면
    stack.append((h, 1)) # 스택에 넣어주기
    continue

  if stack[-1][H] == h: # 스택의 끝 값과 같다면
    cnt = stack.pop()[CNT] # 스택의 끝 값 pop & cnt 추가
    ans += cnt # ans에 cnt 추가

    if stack: # 스택이 비어있지 않다는 것은 마주 볼 수 있는 사람이 있다는 것
      ans += 1
    # 연속인 수들을 하나로 취급하기 위해서 cnt + 1을 추가
    stack.append((h, cnt + 1))

  else:
    stack.append((h, 1))
    ans += 1
    
print(ans)
  