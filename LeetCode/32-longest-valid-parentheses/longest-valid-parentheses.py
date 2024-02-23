class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = [-1]
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            elif len(stack) == 1:
                stack[0] = i
            else:
                stack.pop()
                longest = max(longest, i - stack[-1])
        return longest