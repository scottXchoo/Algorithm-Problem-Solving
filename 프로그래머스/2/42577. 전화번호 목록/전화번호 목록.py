def solution(phone_book):
    answer = True
    hash_map = {}
    
    for ph_num in phone_book:
        hash_map[ph_num] = 1
        
    for ph_num in phone_book:
        temp = ""
        for num in ph_num:
            temp += num
            if temp != ph_num and temp in hash_map:
                return False
    return answer