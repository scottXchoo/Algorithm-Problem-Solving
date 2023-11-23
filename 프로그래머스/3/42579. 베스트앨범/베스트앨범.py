def solution(genres, plays):
    answer = []
    play_map = {}
    genre_map = {}
    # [1] genres를 play의 합을 기준으로 오름차순 정렬
    for idx, genre in enumerate(genres):
        if genre in genre_map:
            genre_map[genre] += plays[idx]
        else:
            genre_map[genre] = plays[idx]
    sorted_genre_map = sorted(genre_map.items(), key= lambda item:item[1], reverse=True)
    # [2] 오름차순 정렬된 해시맵에서 genre를 기준으로 for문
    for genre, _ in list(sorted_genre_map):
        temp = []
        # [3] 각 genre에 맞는 genres의 index를 구해 이를 plays의 값과 함께 temp에 대입
        for idx, _genre in enumerate(genres):
            if _genre == genre:
                temp.append((plays[idx], idx))
        # [4] temp의 0번째 요소는 오름차순, 1번째 요소는 내림차순 순서로 정렬
        temp.sort(key=lambda x: (-x[0], x[1]))
        # [5] 가장 많이 재생된 노래 최대 두 개씩만 보여주기 때문
        temp = temp[:2]
        # [6] 만약 (800, 0), (800, 3)과 같이 play가 중복된다면?
        ## 아래와 같이 play+idx로 key를 만드는 방법으로 해결 (더 좋은 방법 없을까)
        for play, idx in temp:
            play_map[play+idx] = idx

    for i in play_map:
        answer.append(play_map[i])
    
    return answer
