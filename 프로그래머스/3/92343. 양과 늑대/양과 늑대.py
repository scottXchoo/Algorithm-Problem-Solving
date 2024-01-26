def solution(info, edges):
    N = len(info)
    visited = [0] * N
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = False
                
    visited[0] = True
    dfs(1, 0)
    
    return max(answer)