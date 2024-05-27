from collections import defaultdict

N, M = map(int, input().split())

name_dict = defaultdict()
index_dict = defaultdict()

for i in range(N):
    name = input().rstrip()
    name_dict[name] = i + 1
    index_dict[i + 1] = name

for _ in range(M):
    problem = input().rstrip()
    if problem.isdigit():
        print(index_dict[int(problem)])
    else:
        print(name_dict[problem])