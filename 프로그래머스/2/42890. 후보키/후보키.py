from itertools import combinations

def solution(relation):
    row_size = len(relation) # 행 수
    col_size = len(relation[0]) # 열 수
    
    def check_unique(cand, relation): 
        temp = [tuple(item[key] for key in cand) for item in relation]
        if len(set(temp)) == len(temp):
            return True
        return False

    def check_min(cand, cand_keys):
        for key in cand_keys:
            if key.issubset(cand):
                return False
        return True
    
    candidates = [] # 후보키 조합
    for size in range(1, col_size + 1):
        for comb in combinations(range(col_size), size):
            if check_unique(comb, relation) and check_min(comb, candidates):
                candidates.append(set(comb))
                
    return len(candidates)