class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        reachable_node_num, reachable_subnode_num = 0, 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        dist = [maxMoves + 1] * n
        dist[0] = 0
        heap = []
        heappush(heap, (0, 0))

        while heap:
            c_dist, c_node = heappop(heap)
            if maxMoves <= dist[c_node]: # 0에서 시작해야 되니까 특정 노드에서 시작하면 break
                break
            for weight, n_node in graph[c_node]:
                n_dist = c_dist + weight + 1 # 노드 +1 카운트
                if n_dist < dist[n_node]:
                    dist[n_node] = n_dist
                    heappush(heap, (n_dist, n_node))
        
        for d in dist:
            if d <= maxMoves: # maxMoves + 1을 초깃값을 둔 이유
                reachable_node_num += 1

        for u, v, subnode_num in edges:
            a, b = 0, 0
            if dist[u] <= maxMoves:
                a = min(maxMoves - dist[u], subnode_num)
            if dist[v] <= maxMoves:
                b = min(maxMoves - dist[v], subnode_num)
            reachable_subnode_num += min(a + b, subnode_num)

        return reachable_node_num + reachable_subnode_num