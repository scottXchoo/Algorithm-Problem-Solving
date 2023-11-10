N, K = map(int, input().split())
use = list(map(int, input().split()))
plugs = []
ans = 0

for i in range(K):
  if use[i] in plugs: # [1]
    continue

  if len(plugs) < N: # [2]
    plugs.append(use[i])
    continue

  # [3]
  far_one = 0
  temp = 0
  for plug in plugs:
    if plug not in use[i:]: # [4]
      temp = plug
      break

    elif use[i:].index(plug) > far_one: # [5]
      far_one = use[i:].index(plug)
      temp = plug

  plugs[plugs.index(temp)] = use[i]
  ans += 1

print(ans)