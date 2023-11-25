def popAndPush(a, b):
    tmp = a.popleft()
    b.append(tmp)
    return

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
        
        while q2 and q1_sum < q2_sum:
            tmp = q2.popleft()
            q1.append(tmp)
            q2_sum -= tmp
            q1_sum += tmp
            cnt += 1
        
        while q1 and q2_sum < q1_sum:
            tmp = q1.popleft()
            q2.append(tmp)
            q1_sum -= tmp
            q2_sum += tmp
            cnt += 1
            
    answer = cnt
   
    return answer

# <로직 흐름>
# 각 큐에 담긴 모든 원소의 합을 구하고 2로 나눈 값을 target
# q1_sum > q2_sum : a = q1 & b = q2 


# 그 target에 맞게끔 조정
# 그냥 완전탐색인가?
# pop(0) & append : 1, 2 or 2, 1
## 위의 과정이 끝나면, 바로 sum해서 target이랑 맞는지 체크 + (cnt +=1)
### Yes : 끝(answer = cnt) & No : 다시
# 1, 2가 필요하다고 해서 옮기는 방향으로 생각하면, 오히려 많아짐 (차라리 1, 2가 가만히 있고 다른 친구들이 오는 게 더 최솟값일 수도 있음)
# 1) [3, 2, 7, 2, 4] : 18 & [6, 5, 1] : 12
# 2) [2, 7, 2, 4] : 15 & [6, 5, 1, 3] : 15
# [1, 1] : 2 & [1, 5] : 6 => 4
# 1) [1, 1, 1] : 3 & [5] : 5
# 2) [1, 1, 1, 5] : 8 & [0] : 0 =>

# [1] q1 : 14 & q2 : 16
# abs(q1_sum - target) 이게 q1이나 q2에 있다면? (없는 경우도 있음 - 대신 target이 있음)

# [2] q1 : 6 & q2 : 14 => target : 10
# abs(6 - 10) = 4
## q2 = [1, 8, 1, 2] q2 => 12 target => 9 (얘는 target도 q1 or q2에도 없어도 가능함)
## abs(6 - 9) = 3 => 1, 2 옮기면 끝!
## 만약 분해도 안 된다면? 그때는 진짜 -1 리턴?
# 0) [1, 2, 1, 2] : 6 & [1, 10, 1, 2] : 14
# 1) [1, 2, 1, 2, 1] : 7 & [10, 1, 2] : 13
# 2) [1, 2, 1, 2, 1, 10] : 17 & [1, 2] : 3
# 3) [2, 1, 2, 1, 10] : 16 & [1, 2, 1] : 4
# 4) [1, 2, 1, 10] : 14 & [1, 2, 1] : 6
# 5) [2, 1, 10] : 13 & [1, 2, 1, 1] : 7
# 6) [1, 10] : 11 & [1, 2, 1, 1, 2] : 9


# [3] q1 = [1, 1, 1, 1] & q2 = [2, 2, 2, 2] target = 6
## abs(4 - 6) = 2

# <아이디어>
# abs(q1의 합 - target) = dif1
## target보다 큰 값이 있으면 불가능 => -1 (딱 이 경우 밖에 없을까)

# <문제 이해>
# 큐 : A, B
# (A의 원소 pop => B에 insert) * N번 (pop & insert = 1회)
## A와 B의 원소 합을 같도록 만드는 N의 최소 횟수

