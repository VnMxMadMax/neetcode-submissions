# class Solution:
#     def trap(self, height: List[int]) -> int:
#         max_left = height[0]
#         max_rigth = 0
#         storage = 0
#         for h in range(1, len(height)-1):
#             max_right = max(height[h+1:])
#             if height[h] > max_left:
#                 max_left = height[h]
#             elif min(max_left, max_right) < height[h]:
#                 continue
#             else:
#                 current_water = min(max_left, max_right) - height[h]
#                 storage = storage+current_water
#         return storage


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = 0
        right_max = 0
        storage = 0
        left = 0
        right = len(height)-1
        while left<right:
            if height[left] < height[right]:
                storage += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                storage += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1
        return storage
                
        