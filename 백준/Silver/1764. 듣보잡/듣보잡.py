from collections import defaultdict

N, M = map(int, input().split())

noListen = defaultdict(int)
for _ in range(N):
    key = input()
    noListen[key] = 1

answer = 0
lists = []
for _ in range(M):
    key = input()
    if key in noListen:
        answer += 1
        lists.append(key)

lists.sort()
print(answer)
for i in range(len(lists)):
    print(lists[i])