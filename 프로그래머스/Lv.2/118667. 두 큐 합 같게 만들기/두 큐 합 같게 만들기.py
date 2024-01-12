from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(q1), sum(q2)
    cnt = 0
    answer = -1
    
    limit = len(q1) + len(q2)
    diff = q1_sum - q2_sum
    if diff % 2 != 0:
        return -1
    
    while q1_sum != q2_sum:
        if cnt >= limit:
            return -1
        
        while q1_sum < q2_sum:
            temp = q2.popleft()
            q1.append(temp)
            q2_sum -= temp
            q1_sum += temp
            cnt += 1
            
        while q2_sum < q1_sum:
            temp = q1.popleft()
            q2.append(temp)
            q1_sum -= temp
            q2_sum += temp
            cnt += 1
            
    answer = cnt
    
    return answer