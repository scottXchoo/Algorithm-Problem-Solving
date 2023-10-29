x, y, w, h = map(int, input().split())

ans = min(x, y, w - x, h - y)
print(ans)