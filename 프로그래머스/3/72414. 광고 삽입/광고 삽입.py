def solution(play_time, adv_time, logs):
    answer = 0
    
    def times_to_second(times):
        seconds = 0
        h, m, s = times.split(":")
        seconds = int(h) * 3600 + int(m) * 60 + int(s)
        return seconds
        
    def second_to_times(second):
        times = ""
        h = second // 3600
        second -= (h * 3600)
        m = second // 60
        second -= (m * 60)
        times = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(second).zfill(2)
        return times
    
    unit_play_time, unit_adv_time = times_to_second(play_time), times_to_second(adv_time)
    prefix_sum = [0 for _ in range(unit_play_time + 1)]
    
    for log in logs:
        start_time, end_time = log.split("-")
        unit_start_time, unit_end_time = times_to_second(start_time), times_to_second(end_time)
        prefix_sum[unit_start_time] += 1
        prefix_sum[unit_end_time] -= 1
    
    for i in range(1, unit_play_time):
        prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
    
    for i in range(1, unit_play_time):
        prefix_sum[i] = prefix_sum[i] + prefix_sum[i-1]
        
    result = prefix_sum[unit_adv_time - 1]
    for i in range(unit_play_time - unit_adv_time + 1):
        if result < prefix_sum[i + unit_adv_time] - prefix_sum[i]:
            result = prefix_sum[i + unit_adv_time] - prefix_sum[i]
            answer = i + 1
            
    return second_to_times(answer)