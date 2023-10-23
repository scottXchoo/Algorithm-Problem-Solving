L = int(input())
strings = input()
arr = []
add, r = 0, 31

for i in range(L):
  arr.append(ord(strings[i]) - 96)

for idx, num in enumerate(arr):
  add += num * (r ** idx)

print(add % 1234567891)