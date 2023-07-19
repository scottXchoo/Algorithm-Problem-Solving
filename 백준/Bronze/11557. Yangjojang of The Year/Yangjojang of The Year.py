T = int(input())
for _ in range(T):
    N = int(input())
    max = 0
    mName = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if(num > max):
            max = num
            mName = name
    print(mName)