from collections import defaultdict

def solution(id_list, report, k):
    group = defaultdict(set)
    for key_value in report:
        key, value = key_value.split(" ")
        group[key].add(value)
    
    cnts = defaultdict(int)
    for value in group.values():
        for v in value:
            cnts[v] += 1
    
    answer = []
    for i in id_list:
        cnt = 0
        for j in group[i]:
            if cnts[j] >= k:
                cnt += 1
        answer.append(cnt)
    
    return answer