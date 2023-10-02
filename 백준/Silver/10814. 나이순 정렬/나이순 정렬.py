N = int(input())
member_list = []

for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    member_list.append((age, name))
    
member_list.sort(key = lambda x : x[0])

for i in member_list:
    print(i[0], i[1])