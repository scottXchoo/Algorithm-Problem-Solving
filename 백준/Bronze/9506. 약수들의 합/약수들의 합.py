while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")