def solution(nums):  
    answer = 0
    select_num = int(len(nums) / 2)
    unique_types = len(set(nums))
    
    if select_num <= unique_types:
        answer = select_num
    elif unique_types < select_num:
        answer = unique_types
    
    return answer