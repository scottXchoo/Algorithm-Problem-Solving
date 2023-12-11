a, b = map(int, input().split())
c = int(input())
n = int(input())

fn = a*n + b
cgn = c*n

if fn <= cgn and a <= c:
    print(1)
else:
    print(0)