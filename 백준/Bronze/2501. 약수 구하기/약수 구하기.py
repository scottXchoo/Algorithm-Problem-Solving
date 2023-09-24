N, K = map(int, input().split())
arr = []

for i in range(N):
    if(N % (i+1) == 0):
        arr.append(i+1)
        
arr.sort()
if (len(arr) >= K):
  print(arr[K-1])
else:
  print(0)