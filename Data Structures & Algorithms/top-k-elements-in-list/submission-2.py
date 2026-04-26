from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        # Step 1: count frequency
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: fill buckets
        for num, freq in frequency.items():
            bucket[freq].append(num)

        # Step 4: collect top k
        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans