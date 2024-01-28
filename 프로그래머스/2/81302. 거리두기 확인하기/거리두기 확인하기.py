'''
<문제분석>
응시자들끼리 맨해튼 거리 2 이하로 앉지 X
만약, 파티션으로 막혀 있을 경우 허용함

<제한사항>

<아이디어>
각 places의 요소들을 거리두기 여부를 결정하는 함수에 넣는다.
그 함수의 리턴값들을 answer에 넣는다.
'''

from collections import deque

def solution(places):
    answer = []
    
    def is_in_range(r, c):
        return 0 <= r < 5 and 0 <= c < 5
    
    def bfs(r, c, graph):
        visited = [[0] * 5 for _ in range(5)]
        dq = deque()
        dq.append((r, c, 0))
        visited[r][c] = 1
        
        while dq:
            c_r, c_c, dist = dq.popleft()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                n_r = c_r + dr
                n_c = c_c + dc
                n_dist = dist + 1
                if (is_in_range(n_r, n_c) 
                    and graph[n_r][n_c] != "X"
                    and not visited[n_r][n_c]
                     ):
                        if n_dist > 2: continue
                        if place[n_r][n_c] == "P": return 0
                        dq.append((n_r, n_c, n_dist))
                        visited[n_r][n_c] = 1
        return 1
    
    def is_dist(place):
        graph, students = [], []
        for i in range(5):
            temp = []
            for j in range(5):
                temp.append(place[i][j])
                if place[i][j] == "P":
                    students.append((i, j))
            graph.append(temp)

        for r, c in students:
            if bfs(r, c, graph) == 0:
                return 0
        return 1
                        
    for place in places:
        answer.append(is_dist(place))
    return answer