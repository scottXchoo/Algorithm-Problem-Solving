n, m = map(int,input().split())
time = list(map(int,input().split()))

start = max(time)
end = sum(time)

while start <= end:
    mid = (start + end) // 2 

    total = 0
    count = 1
    for t in time:
        if total + t > mid:
            count += 1
            total = 0
        total += t 

    if count <= m:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
    
print(ans)