from collections import defaultdict, deque

def solution(n, computers):
    answer = 0
    graph = defaultdict(list)
    for i, computer in enumerate(computers):
        for j, is_connect in enumerate(computer):
            if is_connect and i < j:
                graph[i].append(j)
                graph[j].append(i)
    nodes = [i for i in range(n)]
    
    def bfs(node):
        dq = deque()
        dq.append(node)
        visited = [0] * n
        visited[node] = 1
        nodes.remove(node)

        while dq:
            c_node = dq.popleft()
            for n_node in graph[c_node]:
                if visited[n_node]:
                    continue
                dq.append(n_node)
                visited[n_node] = 1
                nodes.remove(n_node)
    
    while nodes:
        answer += 1
        bfs(nodes[0])
            
    return answer