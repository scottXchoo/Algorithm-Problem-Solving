def solution(participant, completion):
    hashDict = {}
    sumHash = 0
    
    for par in participant:
        hashDict[hash(par)] = par
        sumHash += hash(par)
        
    for com in completion:
        sumHash -= hash(com)
    
    answer = hashDict[sumHash]
    return answer