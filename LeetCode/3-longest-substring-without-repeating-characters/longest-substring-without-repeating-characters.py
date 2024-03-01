class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer, start = 0, 0
        n = len(s)
        counter = set()
        for idx, c in enumerate(s):
            if c in counter:
                answer = max(answer, idx - start)
                while c in counter:
                    counter.remove(s[start])
                    start += 1
            counter.add(c)
        answer = max(answer, n - start)
        return answer