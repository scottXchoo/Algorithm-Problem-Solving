import heapq

def solution(jobs):
    answer, now, idx = 0, 0, 0
    start = -1
    heap = []
    
    while idx < len(jobs):
        for start_time, duration in jobs:
            if start < start_time <= now:
                heapq.heappush(heap, (duration, start_time))
        if heap:
            duration, start_time = heapq.heappop(heap)
            start = now
            now += duration
            answer += (now - start_time)
            idx += 1
        else:
            now += 1
    
    return answer // len(jobs)