def solution(answers):
    one_list = [1, 2, 3, 4, 5] * 2000
    two_list = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    thr_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    one_cnt, two_cnt, thr_cnt = 0, 0, 0
    length = len(answers)
    result = []
    for ans, ch in zip(answers, one_list[:length]):
        if ans == ch:
            one_cnt += 1
    result.append([1, one_cnt])
    for ans, ch in zip(answers, two_list[:length]):
        if ans == ch:
            two_cnt += 1
    result.append([2, two_cnt])
    for ans, ch in zip(answers, thr_list[:length]):
        if ans == ch:
            thr_cnt += 1
    result.append([3, thr_cnt])

    max_value = 0
    for _, cnt in result:
        max_value = max(max_value, cnt)
        
    answer = []
    for idx, cnt in result:
        if max_value == cnt:
            answer.append(idx)
    
    return answer