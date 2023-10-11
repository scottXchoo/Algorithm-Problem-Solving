import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
ans = []
for _ in range(N):
  ans.append(int(input()))

#1. 산술평균
print(round(sum(ans) / N))

#2. 중앙값
ans.sort()
print(ans[N // 2])

#3. 최빈값
cnt_arr = Counter(ans).most_common()
if len(cnt_arr) > 1 and cnt_arr[0][1] == cnt_arr[1][1]:
  print(cnt_arr[1][0])
else:
  print(cnt_arr[0][0])

#4. 범위
print(max(ans) - min(ans))