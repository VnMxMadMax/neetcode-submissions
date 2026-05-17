class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

        


# nums = [5,3,7,1,7]
# o(nlogn)
# nums = [1,3,5,7,7]
# range(4) = 0,1,2,3