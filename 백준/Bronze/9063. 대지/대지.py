N = int(input())
x_arr, y_arr = [], []

for _ in range(N):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)

x_arr.sort()
y_arr.sort()

x_value = abs(x_arr[0] - x_arr[N-1])
y_value = abs(y_arr[0] - y_arr[N-1])

if N >= 2:
    print(x_value * y_value)
else:
    print(0)