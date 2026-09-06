def solution(tickets):
    tickets.sort()
    visited = [False] * len(tickets)
    answer = ["ICN"]
    
    def dfs(depth, cur):
        if depth == len(tickets):
            return True
        
        for i in range(len(tickets)):
            start, end = tickets[i]
            if start == cur and not visited[i]:
                answer.append(end)
                visited[i] = True
                
                if dfs(depth + 1, end):
                    return True
                
                answer.pop()
                visited[i] = False
        return False
    
    dfs(0, "ICN")
    return answer

# ICN에서 출발
# tickets: a => b
# 가능한 경로 2개 이상이면 알파벳 순서가 앞서도록
# 목표: 방문하는 공항 경로
# 딕셔너리?