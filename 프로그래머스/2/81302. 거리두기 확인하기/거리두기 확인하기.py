'''
<문제 분석>
맨해튼 거리 3부터 가능
응시자들 사이에 파티션으로 막혀 있다면, 괜찮음
각 대기실별로 거리두기를 잘 지키고 있으면, 1 & 한 명이라도 지키지 않으면, 0

<제한 사항>
places의 행 길이(대기실 개수) = 5
대기실의 가로 & 세로 길이 : 각각 5

<아이디어>
각 행에 대해서 거리두기가 잘 지켜졌는지 아닌지를 판단하여 result에 값 넣기
각 행이 현재 문자열인데, 이를 하나씩 나눠야할 듯?
P를 기준으로 맨해튼 거리가 2이하까지만 체크하면 됨 (3이상은 의미 X)
맨해튼 거리 2이하인데, P면?
- X(파티션)이 그 전 노드에 있는지 없는지
P가 아니면, 당연히 볼 필요 X
=> BFS 사용하면 되겠다!
'''

from collections import deque

def solution(places):
    answer = []
    N = len(places)
    
    def is_in_range(r, c):
        return 0 <= r < N and 0 <= c < N
    
    def bfs(r, c, graph, visited):
        dq = deque()
        dq.append((r, c, 0))
        visited[r][c] = 1
        
        while dq:
            c_r, c_c, dist = dq.popleft()
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                n_r = c_r + dr
                n_c = c_c + dc
                n_dist = dist + 1
                if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
                    if n_dist <= 2:
                        if graph[n_r][n_c] == "P":
                            if graph[c_r][c_c] != "X":
                                return 0
                        else: # "O" or "X"
                            dq.append((n_r, n_c, n_dist))
                            visited[n_r][n_c] = 1
        return 1
    
    def is_okay(place):
        # 각 대기실을 받아서 거리두기가 잘 되고 있는지 판단하는 함수
        ## return은 0 또는 1
        # 1. 이 place를 분해(?)해야 됨
        # 2. p의 위치를 리스트에 저장한 뒤, 하나씩? (대신, visited는 전역으로)
        # 3. 각 p의 위치마다 BFS 돌리기
        ## 만약 한 개라도 거리두기가 안 되면, 다른 p를 탐색할 필요 X => 바로 break 걸고 return 때리기
        graph, p_pos = [], []
        for i in range(N):
            arr = []
            for j in range(N):
                arr.append(place[i][j])
                if place[i][j] == "P":
                    p_pos.append((i, j))
            graph.append(arr)
            
        visited = [[0] * N for _ in range(N)]
        for r, c in p_pos:
            if bfs(r, c, graph, visited) == 0: # 거리두기 실패면, 바로 0 리턴해서 종료시키기
                return 0
        return 1 # for문 끝까지 탐색했는데, 0이 나오지 않았다는 얘기는 거리두기 잘 지켰다는 의미
            
    
    for place in places:
        result = is_okay(place)
        answer.append(result)
    
    return answer