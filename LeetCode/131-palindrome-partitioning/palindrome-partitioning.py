from collections import deque

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalin(c):
            return c == c[::-1]

        def backtrack(s, curr):
            if len(s) == 0:
                result.append(curr[:])
                return

            for i in range(1, len(s)+1):
                c = s[:i]
                if c and isPalin(c):
                    curr.append(c)
                    backtrack(s[i:], curr)
                    curr.pop()
                
        result = []
        backtrack(s, [])
        return result