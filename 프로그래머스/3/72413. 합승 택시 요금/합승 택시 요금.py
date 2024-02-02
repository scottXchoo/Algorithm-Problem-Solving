from collections import defaultdict
from heapq import heappop, heappush
import sys

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, w in fares:
        graph[u].append((w, v))
        graph[v].append((w, u))
        
    answer = sys.maxsize
    costs = [[sys.maxsize for _ in range(n+1)] for _ in range(3)]
    
    for idx, s_node in enumerate([s, a, b]):
        heap = []
        heappush(heap, (0, s_node))
        costs[idx][s_node] = 0
        
        while heap:
            c_cost, c_node = heappop(heap)
            for cost, n_node in graph[c_node]:
                n_cost = c_cost + cost
                if n_cost < costs[idx][n_node]:
                    costs[idx][n_node] = n_cost
                    heappush(heap, (n_cost, n_node))
        
        for idx in range(n+1):
            answer = min(answer, costs[0][idx] + costs[1][idx] + costs[2][idx])
    
    return answer