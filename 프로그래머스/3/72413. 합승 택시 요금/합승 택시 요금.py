from collections import defaultdict
from heapq import heappop, heappush
import sys

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for u, v, w in fares:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    def mid_dijkstra(start, mid):
        visited = [sys.maxsize] * (n + 1)
        visited[start] = 0
        pq = []
        heappush(pq, (0, start))
        
        while pq:
            c_fare, c_node = heappop(pq)
            for fare, n_node in graph[c_node]:
                n_fare = fare + c_fare
                if n_fare < visited[n_node]:
                    visited[n_node] = n_fare
                    heappush(pq, (n_fare, n_node))
                    
        return mid, visited[mid]
    
    def dijkstra(mid, m_fare):
        visited = [sys.maxsize] * (n + 1)
        visited[mid] = m_fare
        pq = []
        heappush(pq, (m_fare, mid))
        
        while pq:
            c_fare, c_node = heappop(pq)
            for fare, n_node in graph[c_node]:
                n_fare = fare + c_fare
                if n_fare < visited[n_node]:
                    visited[n_node] = n_fare
                    heappush(pq, (n_fare, n_node))
                    
        return visited[a], visited[b]
    
    arr = []
    for m in range(1, n+1):
        ans = 0
        m_node, m_fare = mid_dijkstra(s, m)
        a_fare, b_fare = dijkstra(m_node, m_fare)
        ans = a_fare + b_fare - m_fare
        arr.append(ans)
    
    return min(arr)