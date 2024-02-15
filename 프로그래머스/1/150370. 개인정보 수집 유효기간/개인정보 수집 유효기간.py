from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    # 날짜와 추가할 기간 => 날짜 + 기간
    def calc_date(date, term):
        y, m, d = date.split(".")
        m_t = int(m) + term
        # if m_t % 12 == 0:
        #     add_y = m_t // 12 - 1
        #     add_m = int(m)
        if m_t > 12:
            if m_t % 12 == 0:
                add_y = m_t // 12 - 1
                add_m = m_t % 12
                if add_m == 0:
                    add_m = 12
            else:
                add_y = m_t // 12
                add_m = m_t % 12
        else:
            add_y = 0
            add_m = m_t
        
        n_y = int(y) + add_y
        n_m = add_m
        n_date = str(n_y) + "." + str(n_m).zfill(2) + "." + d
        
        return n_date
        
    # terms로 딕셔너리 만들기
    term_dict = defaultdict(int)
    for term in terms:
        x, y = term.split(" ")
        term_dict[x] = y

    # privacies로 answer 구하기 with today
    for idx, privacy in enumerate(privacies):
        date, x = privacy.split()
        y = term_dict[x]
        n_date = calc_date(date, int(y))
        print("n_date", n_date)

        if n_date <= today:
            answer.append(idx + 1)
    
    return answer