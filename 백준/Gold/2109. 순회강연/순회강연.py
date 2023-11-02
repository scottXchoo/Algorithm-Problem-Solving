import heapq

n = int(input())
lectures = []
for _ in range(n):
    p, d = map(int, input().split())
    lectures.append((d, p))

lectures.sort()
result = 0
q = []

for lecture in lectures:
    d, p = lecture
    heapq.heappush(q, p)
    if len(q) > d:
        heapq.heappop(q)

print(sum(q))
