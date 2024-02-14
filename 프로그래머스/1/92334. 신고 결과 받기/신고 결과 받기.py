from collections import defaultdict

def solution(id_list, report, k):
    group = defaultdict(set)
    count = defaultdict(int)
    for key_value in report:
        key, value = key_value.split(" ")
        group[key].add(value)
        count[(key, value)] = 1
    
    cnts = defaultdict(int)
    for key, value in count:
        cnts[value] += 1
    
    answer = []
    for i in id_list:
        cnt = 0
        for j in group[i]:
            if cnts[j] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer