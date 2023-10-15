import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10000

for _ in range(N):
    a = int(input())
    arr[a-1] += 1
    
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)