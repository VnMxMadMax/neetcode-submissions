class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        


# nums = [5,3,7,1,7]
# o(nlogn)
# nums = [1,3,5,7,7]
# range(4) = 0,1,2,3