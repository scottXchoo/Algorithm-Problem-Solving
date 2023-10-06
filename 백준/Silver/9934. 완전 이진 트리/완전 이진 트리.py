K = int(input())
inorder = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def recur(arr, dep):
  mid = len(arr) // 2
  tree[dep].append(arr[mid])
  if len(arr) == 1:
    return
  recur(arr[:mid], dep+1)
  recur(arr[mid+1:], dep+1)

recur(inorder, 0)
for i in tree:
  print(*i)