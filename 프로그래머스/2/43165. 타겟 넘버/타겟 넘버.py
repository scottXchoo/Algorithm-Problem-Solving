def solution(numbers, target):
    answer = 0
    # numbers 각 숫자마다 더할지 뺄지 판단하기
    # 각 숫자마다 더할지 말지 판단해서 target이 되면 카운트 업
    # DFS 사용
    def dfs(index, cur_num):
        nonlocal answer
        if index == len(numbers):
            if cur_num == target:
                answer += 1
            return
        dfs(index+1, cur_num + numbers[index])
        dfs(index+1, cur_num - numbers[index])
    dfs(0, 0)
    
    return answer

# n개 양수
# 순서 변경 X, 적절히 더하거나 빼서 => 타겟 숫자
# numbers 2^20번 연산 필요