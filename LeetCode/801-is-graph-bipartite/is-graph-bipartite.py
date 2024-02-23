class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        global answer
        n = len(graph)
        graphs, colors = {}, {}
        answer = True
        for i, g in enumerate(graph):
            graphs[i] = g
            colors[i] = 0
        
        def visited_color(depth, node, colors):
            if depth % 2 == 0:
                colors[node] = 1
            else:
                colors[node] = 2
        
        def dfs(depth, node, graphs, colors):
            global answer
            if answer == False:
                return
            
            visited_color(depth, node, colors)
            for n_node in graph[node]:
                if colors[n_node] != 0 and colors[n_node] == colors[node]:
                    answer = False
                    break
                if colors[n_node] == 0:
                    dfs(depth+1, n_node, graphs, colors)
        
        for i in range(n):
            if colors[i] == 0:
                dfs(0, i, graphs, colors)
                
        return answer