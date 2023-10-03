N = int(input())
nums = map(int, input().split())
sosu = 0

for num in nums:
    err = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 num - 1까지
            if num % i == 0:
                err += 1  # 2부터 num - 1까지 나눈 몫이 0이면 error가 증가
        if err == 0:
            sosu += 1  # error가 없으면 소수
print(sosu)
