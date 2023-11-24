def calc_n(X, Y): # X와 Y 모두 {} 형태
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x + y)
            n_set.add(x - y)
            n_set.add(x * y)
            if y != 0:
                n_set.add(x // y)
    return n_set # +, -, *, / 모든 경우를 다 넣어서 리턴

def solution(N, number):
    answer = -1
    result = {}
    result[1] = {N}
    if N == number:
        return 1
    
    for n in range(2, 9):
        temp_set = {int(str(N) * n)} # N이 5일 때: 5, 55, 555, ...
        i = 1
        # update 사용 : 5+1, 1+5의 중복 막음
        # result[i], result[n-i] : 5-1, 1-5의 다름을 구별함
        while i < n:
            temp_set.update(calc_n(result[i], result[n-i]))
            i += 1
            
        if number in temp_set:
            answer = n
            break
        
        result[n] = temp_set
    
    return answer