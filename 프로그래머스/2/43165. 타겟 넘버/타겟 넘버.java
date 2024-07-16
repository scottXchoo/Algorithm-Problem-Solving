/**
문제분석
- n개의 음이 아닌 정수
- 이 정수들을 순서 바꾸지 않고 적절히 더하거나 빼기
- 목표 : target이 되도록

제한사항
- 주어진 숫자의 개수 2개 이상 20개 이하
- 각 숫자는 1 이상 50 이하인 자연수
- 타겟 넘버는 1 이상 1000 이하

아이디어
- DFS로 각 위치(depth)의 부호를 (+) or (-)로 설정해서 값 구하기
- 마지막 위치까지 왔을 때, target이면 answer++ & return
- 각 depth에 해당하는 number 앞에 부호를 더하거나 빼거나
- 현재 값 num & 다음 값 numbers[depth]
- dfs(num + numbers[depth], depth + 1, target,  numbers)
- dfs(num - numbers[depth], depth + 1, target, numbers)
**/
class Solution {
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        dfs(0, 0, target, numbers);
        return answer;
    }
    
    private static void dfs(int num, int depth, int target, int[] numbers) {
        if (depth == numbers.length) {
            if (target == num) answer++;
            return;
        }
        
        dfs(num - numbers[depth], depth + 1, target, numbers);
        dfs(num + numbers[depth], depth + 1, target, numbers);
    }
}