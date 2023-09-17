num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일 경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일 경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')