class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans = []
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        pairs = list(frequency.items())
        pairs.sort(key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(pairs[i][0])
        return ans