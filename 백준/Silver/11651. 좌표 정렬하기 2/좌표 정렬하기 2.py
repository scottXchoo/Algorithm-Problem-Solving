import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([y, x])
    
s_arr = sorted(arr)

for y, x in s_arr:
    print(x, y)