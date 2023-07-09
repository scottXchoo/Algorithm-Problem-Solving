cnt = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[0], array[-1])