import sys, copy

def solution(s):
    answer = 0
    length = len(s)
    
    def check_slice(slice_num, s):
        cnt = 1
        word = s[:slice_num]
        s = s[slice_num:]
        
        while word == s[:slice_num]:
            cnt += 1
            s = s[slice_num:]
        
        return cnt, word, s

    answer = sys.maxsize
    for slice_num in range(1, length+1):
        temp = copy.copy(s)
        ans = ""
        while len(temp) != 0:
            cnt, word, temp = check_slice(slice_num, temp)
            if cnt != 1:
                ans += str(cnt) + str(word)
            else:
                ans += str(word)
                
        if len(ans) != 0:
            answer = min(answer, len(ans))
    
    return answer