class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        current_string = set()
        max_string = 1
        s = list(s)
        if len(s) == 0:
            return 0
        current_string.add(s[l])
        while r < len(s):
            if s[r] not in current_string:
                current_string.add(s[r])
                max_string = max(len(current_string), max_string)
                r += 1
            else:
                while s[r] in current_string:
                    current_string.remove(s[l])
                    l += 1
        return max_string




        l,r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            elif prices[r] >= prices[l]:
                current_profit = prices[r]- prices[l]
                max_profit = max(max_profit, current_profit)
                r += 1
        return max_profit
        