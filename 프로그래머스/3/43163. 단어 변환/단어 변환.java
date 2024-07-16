/**
문제분석
- begin의 단어에서 target 단어로 변환
- 목표 : 변환하는 데 최소 몇 단계의 과정을 거치는지 구하기

제한사항
- words 안에 target이 애초에 없으면, return 0이네?

아이디어
- begin에서 딱 한 개의 단어만 다른 단어를 words에서 찾고
- 그 단어에서 또 한 개의 단어만 다른 단어를 words에서 찾고 ...
- 하나라도 같은 단어가 있으면, 그래프처럼 연결시키자
- BFS로 탐색하다가 해당 단어가 target이면, 종료 & 그때까지 카운트한 숫자가 정답
- 1) words로 그래프 만들기
- 2) 그 그래프 BFS로 탐색하기
- 3) 

**/
import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        Map<String, List<String>> graph = buildGraph(begin, words);
        
        // target이 words 배열에 없으면 0 return
        if (!graph.containsKey(target)) return 0;
        
        // // 그래프 출력
        // for (String word : graph.keySet()) {
        //     System.out.println(word + " -> " + graph.get(word));
        // }
        
        Queue<String> queue = new LinkedList<>();
        Map<String, Integer> visited = new HashMap<>();
        
        queue.add(begin);
        visited.put(begin, 0);
        
        while (!queue.isEmpty()) {
            String current = queue.poll();
            
            // target에 도달하면, 지금까지 변환된 개수 return
            if (current.equals(target)) {
                return visited.get(current);
            }
            
            for (String next : graph.get(current)) {
                if (!visited.containsKey(next)) {
                    queue.add(next);
                    visited.put(next, visited.get(current) + 1);
                }
            }
        }
        
        return 0;
    }
    
    private static Map<String, List<String>> buildGraph(String begin, String[] words) {
        List<String> allWords = new ArrayList<>(Arrays.asList(words));
        allWords.add(begin);
        
        Map<String, List<String>> graph = new HashMap<>();
        for (String word : allWords) {
            graph.put(word, new ArrayList<>());
        }
        
        for (int i = 0; i < allWords.size(); i++) {
            for (int j = i + 1; j < allWords.size(); j++) {
                if (isOneCharDiff(allWords.get(i), allWords.get(j))) {
                    graph.get(allWords.get(i)).add(allWords.get(j));
                    graph.get(allWords.get(j)).add(allWords.get(i));
                }
            }
        }
        return graph;
    }
    
    private static boolean isOneCharDiff(String word1, String word2) {
        int count = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                count++;
            }
        }
        if (count > 1) return false;
        else return true;
    }
}