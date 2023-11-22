def solution(clothes):
    answer = 0
    hash_map = {}
    for cloth in clothes:
        types = cloth[1]
        if types in hash_map:
            hash_map[types] += 1
        else:
            hash_map[types] = 1
            
    sum = 1
    for types in list(hash_map):
        sum *= hash_map[types] + 1
    answer = sum - 1
    
    return answer

# hash_map = {고유한 종류에 대한 값은 넣을 수 있겠다}
# hash_map = {"face" : cnt}
# hash_map = {"headgear" : 2, "eyewear" : 1} = {"face" : 3}
# hash_map = {"headgear" : 2, "eyewear" : 1, "face" : 2} = {"face" : 3}

# 각 키에 대한 값+1을 키의 개수에 맞게 곱해주고 - 1(하나라도 입어야하기 때문)
