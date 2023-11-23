def solution(genres, plays):
    answer = []
    genre_list = []
    test_map = {}
    plays_map = {}
    hash_map = {}
    
    for idx, genre in enumerate(genres):
        if genre in hash_map:
            hash_map[genre] += plays[idx]
        else:
            hash_map[genre] = plays[idx]
    sorted_map = sorted(hash_map.items(), key= lambda item:item[1], reverse=True)
    
    for g in sorted_map:
        genre_list.append(g[0])
    for genre in genre_list:
        temp = []
        # genres에서 genre에 맞는 index를 구하고 이를 plays에 대입
        for i, g in enumerate(genres):
            if g == genre:
                temp.append((plays[i], i))
        print("temp(1)", temp)
        temp.sort(key=lambda x: (-x[0], x[1]))
        print("temp(2)", temp)
        temp = temp[:2]
        print("temp(3)", temp)
        for play, idx in temp:
            test_map[play+idx] = idx
            
    for i in test_map:
        answer.append(test_map[i])
    print(answer)
    
    return answer

# 각 장르별로 길이 합해서 정렬? | "pop", "classic"
# 장르 내에서 오름차순 정렬 & 딱 2개까지만 | "pop" : 2500, 600 & "classic" : 800, 500
# 각 길이들에 대한 인덱스를 순서대로 answers에 넣어주기
# answers에 인덱스가 들어가야 됨 => 어떤 식으로? pop 쭉, classic 쭉 ...
# {pop: {2500 : 4, 600 : 1}, classic: {800 : 3, 500 : 0}}

# 노래끼리는 오름차순
# 장르 내에서 많이 재생된 노래 먼저
# 속한 노래가 많이 재생된 장르 먼저
# 에이 일단 다 더하는거네
## hash_map
# classic : 500 + 800 (150 X)
# pop : 600 + 2500
# pop > classic
## pop : 2500(4), 600(1)
## classic : 800(3), 500(0)

# for i, g in enumerate(genre_list): # genre : pop => classic
    #     for j, genre in enumerate(genres):
    #         if g == genre:
    #             test_map[g] = [plays[j]]
    #         # if g == genre:
    #         #     plays_map[plays[j]] = [j, 1]