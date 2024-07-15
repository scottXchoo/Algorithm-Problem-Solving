import java.util.*;
class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
        
        for (int i = 0; i < computers.length; i++) {
            for (int j = i + 1; j < computers[i].length; j++) {
                if (computers[i][j] == 1) {
                    graph.get(i).add(j);
                    graph.get(j).add(i);
                }
            }
        }
        
        List<Integer> nodes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nodes.add(i);
        }
        
        while (!nodes.isEmpty()) {
            answer++;
            bfs(nodes.get(0), graph, nodes, n);
        }
        
        return answer;
    }
    
    private void bfs(int node, Map<Integer, List<Integer>> graph, List<Integer> nodes, int n) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        boolean[] visited = new boolean[n];
        visited[node] = true;
        nodes.remove(Integer.valueOf(node));
        
        while (!queue.isEmpty()) {
            int currentNode = queue.poll();
            for (int nextNode : graph.get(currentNode)) {
                if (visited[nextNode]) continue;
                
                queue.add(nextNode);
                visited[nextNode] = true;
                nodes.remove(Integer.valueOf(nextNode));
            }
        }
    }
}