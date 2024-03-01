class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx, [u, v] in enumerate(edges):
            prob = succProb[idx]
            graph[u].append((-prob, v))
            graph[v].append((-prob, u))

        def dijkstra(graph, start, end):
            probs = [1] * n
            pq = [(-1, start)]
            probs[start] = -1

            while pq:
                c_prob, c_node = heapq.heappop(pq)
                for prob, n_node in graph[c_node]:
                    n_prob = c_prob * prob * -1
                    if n_prob < probs[n_node]:
                        probs[n_node] = n_prob
                        heapq.heappush(pq, (n_prob, n_node))
            return abs(probs[end])

        ans = dijkstra(graph, start_node, end_node)
        if ans == 1:
            return 0.00000
        else:
            return round(ans, 5)