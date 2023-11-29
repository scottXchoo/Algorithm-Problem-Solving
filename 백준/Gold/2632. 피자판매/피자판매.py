from collections import deque
import sys
ipt = sys.stdin.readline


def init():
    total = int(ipt())
    m, n = map(int, ipt().split())
    a = [int(ipt()) for _ in range(m)]
    b = [int(ipt()) for _ in range(n)]
    return a, m, b, n, total
    

def get_count(a, m):
    count_a = [0] * (sum(a) + 1)
    count_a[0] = 1
    count_a[-1] = 1
    for i in range(m):
        q = deque(a)
        for _ in range(i):
            q.rotate(-1)
        q.pop()
        summ = 0
        while q:
            summ += q.popleft()
            count_a[summ] += 1
    return count_a


a, m, b, n, total = init()
count_a = get_count(a, m)
count_b = get_count(b, n)
answer = 0
for i in range(total + 1):
    j = total - i
    if 0 <= i < len(count_a) and 0 <= j < len(count_b):
        answer += count_a[i] * count_b[j]
print(answer)