class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        answer = 0
        M, N = len(heightMap), len(heightMap[0])
        dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
        visited = [[False] * N for _ in range(M)]
        heap = []

        def is_in_range(r, c):
            return 0 <= r < M and 0 <= c < N

        for i in range(M):
            for j in range(N):
                if i == 0 or i == M-1:
                    heapq.heappush(heap, (heightMap[i][j], [i, j]))
                    visited[i][j] = True
                elif j == 0 or j == N-1:
                    heapq.heappush(heap, (heightMap[i][j], [i, j]))
                    visited[i][j] = True

        while heap:
            (c_h, [c_r, c_c]) = heapq.heappop(heap)
            
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                n_r = c_r + dr
                n_c = c_c + dc
                if is_in_range(n_r, n_c) and not visited[n_r][n_c]:
                    n_h = heightMap[n_r][n_c]
                    answer += max(0, c_h - n_h)
                    visited[n_r][n_c] = True

                    heapq.heappush(heap, (max(c_h, n_h), [n_r, n_c]))

        return answer