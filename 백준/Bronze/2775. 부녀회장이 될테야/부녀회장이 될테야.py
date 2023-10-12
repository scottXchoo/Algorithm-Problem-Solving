T = int(input())

for i in range(T):
    K = int(input())
    N = int(input())
    people = [i for i in range(1, N+1)]
    
    for x in range(K):
        for y in range(1, N):
            people[y] += people[y-1]
    print(people[-1])