class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left, right = 0, len(height) - 1

        while left != right:
            if height[left] <= height[right]:
                n_left_idx = left + 1
                if height[n_left_idx] < height[left]:
                    answer += height[left] - height[n_left_idx]
                    height[n_left_idx] = height[left] # 메꿔가면서 계산하기
                left = n_left_idx
            else:
                n_right_idx = right - 1
                if height[n_right_idx] < height[right]:
                    answer += height[right] - height[n_right_idx]
                    height[n_right_idx] = height[right]
                right = n_right_idx

        return answer

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         answer = 0
#         stack = []
#         trapped = height[:]
#         popElement = (0, 0)
#         for i, h in enumerate(height):
#             while stack and h >= stack[-1][1]:
#                 popElement = stack.pop()

#             if stack:
#                 left_idx, _ = stack[-1]
#                 for j in range(left_idx+1, i):
#                     trapped[j] = h
#             else:
#                 left_idx, left_h = popElement
#                 for j in range(left_idx+1, i):
#                     trapped[j] = left_h
#             stack.append((i, h))

#         for i in range(len(height)):
#             diff = trapped[i] - height[i]
#             answer += diff

#         return answer