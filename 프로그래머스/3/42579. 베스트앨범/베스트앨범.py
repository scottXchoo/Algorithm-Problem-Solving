def solution(genres, plays):
    answer = []
    genreDict = {genre:[] for genre in set(genres)} # {'classic': [], 'pop': []}
    for e in zip(genres, plays, range(len(plays))): # ('classic', 500, 0), ('pop', 600, 1), ...
        # genreDict[e[0]] : []
        genreDict[e[0]].append([e[1], e[2]]) # {'pop': [[600, 1], [2500, 4]], 'classic': [[500, 0], [150, 2], [800, 3]]}
    genreSort = sorted(list(genreDict.keys()), key = lambda x: sum(t[0] for t in genreDict[x]), reverse = True)
    for genre in genreSort:
        # e : [150, 2], e[1] : 고유 번호(2), x[0] : 재생된 횟수(150), x[1] : 고유 번호(2)
        # x[0]은 내림차순 그 이후, x[1]은 오름차순
        temp = [e[1] for e in sorted(genreDict[genre], key = lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp), 2)] # 최대 2까지 자르는 방법

    return answer