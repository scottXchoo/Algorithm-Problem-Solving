import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
  if card in count:
    count[card] += 1
  else:
    count[card] = 1

for target in candidate:
  # 딕셔너리의 get : 첫번째 인자인 키의 값 혹은 두번째 인자 리턴\
  ## 두번째 인자의 디폴트 = None
  result = count.get(target, 0)
  if result == 0:
    print(0, end = " ")
  else:
    print(result, end = " ")