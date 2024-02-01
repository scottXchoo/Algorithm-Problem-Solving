from collections import defaultdict
from heapq import heappush, heappop

def solution(n, paths, gates, summits):
    answer = []
    summits.sort()
    summit_set = set(summits)
    
    def find():
        graph = defaultdict(list)
        for u, v, w in paths:
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        pq = []
        # 1번부터 n번까지 노드이기에 (n + 1)개 공간 필요
        visited = [10000001] * (n + 1)
        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate] = 0
        
        while pq:
            intensity, c_node = heappop(pq)
            if intensity > visited[c_node] or c_node in summit_set:
                continue
                
            for weight, n_node in graph[c_node]:
                n_intensity = max(weight, intensity)
                if n_intensity < visited[n_node]:
                    visited[n_node] = n_intensity
                    heappush(pq, (n_intensity, n_node))
                    
        min_intensity = [0, 10000001]
        for summit in summits:
            if min_intensity[1] > visited[summit]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]

        return min_intensity
    
    answer = find()
            
    # answer.sort(key = lambda x :(x[1], x[0]))
        
    return answer