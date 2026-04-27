# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [1] * n

#         left_product = 1
#         for i in range(n):
#             ans[i] = left_product
#             print(f"left_ans: {ans}")
#             left_product *= nums[i]
#             print(f"left_product: {left_product}")

#         right_product = 1
#         for i in range(n-1, -1, -1):
#             ans[i] *= right_product
#             print(f"right_ans: {ans}")
#             right_product *= nums[i]
#             print(f"right_product: {right_product}")

#         return ans

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # Left products
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product *= nums[i]

        # Right products
        right_product = 1
        for i in range(n-1, -1, -1):
            ans[i] *= right_product
            right_product *= nums[i]

        return ans