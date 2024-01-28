'''
<문제분석>
ShiftRow : 모든 행이 아래쪽으로 한 칸씩 밀려난다.
- left, mid, right 큐를 만든다.
- 각 큐의 맨 마지막 요소를 맨 처음에 넣어준다.

Rotate : 행렬의 바깥쪽에 있는 원소들을 시계 방향으로 한 칸씩 회전시키기.
- left, mid, right 큐를 만든다.
- left의 첫 요소 => mid 처음에 넣기
- mid의 첫 요소 => right 처음에 넣기
- right의 끝 요소 => mid 끝에 넣기
- mid의 끝 요소 => left 끝에 넣기

<제한사항>
정확성과 효율성 테스트 각각 점수 존재
operations이 10^6 ?! 빡세다...

<아이디어>
큐를 이용해서 풀면 될 듯
'''

from collections import deque

def solution(rc, operations):
    n, m = len(rc), len(rc[0])
    left = deque([])
    mid = deque([])
    right = deque([])
    
    for i in range(n):
        tmp_mid = deque([])
        for j in range(m):
            if j == 0:
                left.append(rc[i][j])
            elif j == m-1:
                right.append(rc[i][j])
            else:
                tmp_mid.append(rc[i][j])
        mid.append(tmp_mid)
    
    def shiftRow(left, right, mid):
        left.appendleft(left.pop())
        right.appendleft(right.pop())
        mid.appendleft(mid.pop())
            
    def rotate(left, right, mid):
        mid[0].appendleft(left.popleft())
        right.appendleft(mid[0].pop())
        mid[n-1].append(right.pop())
        left.append(mid[n-1].popleft())
        
    for operation in operations:
        if operation == "Rotate":
            rotate(left, right, mid)
        elif operation == "ShiftRow":
            shiftRow(left, right, mid)
            
    for i in range(n):
        for j in range(m):
            if j == 0:
                rc[i][j] = left[i]
            elif j == m-1:
                rc[i][j] = right[i]
            else:
                rc[i][j] = mid[i][j-1]
    return rc