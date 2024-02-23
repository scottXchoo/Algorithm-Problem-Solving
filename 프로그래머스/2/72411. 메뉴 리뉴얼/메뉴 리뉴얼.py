from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
                
    for k in course:
        candidates = []
        for order in orders:
            candidates.extend(combinations(sorted(order), k))
            
        common = Counter(candidates).most_common()
        for c, cnt in common:
            if cnt >= 2 and cnt == common[0][1]:
                answer.append(''.join(c))

    answer.sort()
    return answer