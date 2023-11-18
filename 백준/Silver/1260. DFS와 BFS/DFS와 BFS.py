from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visitedB = [False] * (N + 1)
visitedD = [False] * (N + 1)

def bfs(V):
    dq = deque([V])
    visitedB[V] = True
    while dq:
        V = dq.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not visitedB[i] and graph[V][i]:
                dq.append(i)
                visitedB[i] = True
                
def dfs(V):
    visitedD[V] = True
    print(V, end=" ")
    for i in range(1, N + 1):
        if not visitedD[i] and graph[V][i]:
            dfs(i)
            
dfs(V)
print()
bfs(V)