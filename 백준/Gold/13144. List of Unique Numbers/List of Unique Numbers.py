N = int(input())
num_list = list(map(int, input().split()))

result = 0
start, end = 0, 0
seq = [False for _ in range(1000001)]
while start < N and end < N:
  if not seq[num_list[end]]:  # start부터 end까지 중복 숫자 없으면
    seq[num_list[end]] = True
    end += 1
    result += (end - start)  # end를 포함하여 만들 수 있는 수열의 개수
  else:
    seq[num_list[start]] = False
    start += 1

print(result)