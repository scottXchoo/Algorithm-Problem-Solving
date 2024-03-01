class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dq = deque()
        t_cnt = defaultdict(int)
        for c in t:
            t_cnt[c] += 1
        answer = "1" * 100001
        remain = len(t)
        for i, c in enumerate(s):
            if c in t_cnt:
                dq.append((i, c))
                if t_cnt[c] > 0:
                    remain -= 1
                t_cnt[c] -= 1
                while not remain:
                    start, end = dq[0][0], dq[-1][0]
                    s_start = s[start]
                    if s_start in t_cnt:
                        t_cnt[s_start] += 1
                        if t_cnt[s_start] > 0:
                            remain += 1
                            if end - start < len(answer):
                                answer = s[start:end+1]
                    dq.popleft()

        if len(answer) < 100000:
            return answer
        else:
            return ""