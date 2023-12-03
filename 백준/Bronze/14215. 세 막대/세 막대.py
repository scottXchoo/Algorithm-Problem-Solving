li = sorted(map(int, input().split()))
res = li[0] + li[1] + min(li[2], li[0]+li[1]-1)

print(res)