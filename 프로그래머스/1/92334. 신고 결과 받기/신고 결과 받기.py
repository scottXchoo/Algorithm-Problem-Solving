def solution(id_list, report, k):
    report_set = set(report)
    answer = [0] * len(id_list)
    reports = {x: 0 for x in id_list}
    for r in report_set:
        _, value = r.split()
        reports[value] += 1
        
    for r in report_set:
        key, value = r.split()
        if reports[value] >= k:
            answer[id_list.index(key)] += 1
    
    return answer