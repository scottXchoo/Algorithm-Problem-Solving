class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        if len(prerequisites) != 0:
            for u, v in prerequisites:
                graph[v].append(u)
                indegree[u] += 1
        else:
            for i in range(numCourses):
                answer.append(i)
                answer.reverse()
            return answer

        dq = deque()
        path = []
        for course in range(numCourses):
            if course not in indegree:
                path.append(course)
                dq.append(course)

        while dq:
            c_node = dq.popleft()
            for n_node in graph[c_node]:
                indegree[n_node] -= 1

                if indegree[n_node] == 0:
                    path.append(n_node)
                    dq.append(n_node)

        if len(path) == numCourses:
            answer = path
        else:
            answer = []

        return answer    