def solution(survey, choices):
    answer = ""
    dict = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    
    for i in range(len(survey)):
        if choices[i] > 4: # 5, 6, 7
            dict[survey[i][1]] += choices[i] - 4 # 1, 2, 3
        elif choices[i] < 4: # 1, 2, 3
            dict[survey[i][0]] += 4- choices[i] # 3, 2, 1
    
    answer += "R" if dict["R"] >= dict["T"] else "T"
    answer += "C" if dict["C"] >= dict["F"] else "F"
    answer += "J" if dict["J"] >= dict["M"] else "M"
    answer += "A" if dict["A"] >= dict["N"] else "N"
    
    return answer