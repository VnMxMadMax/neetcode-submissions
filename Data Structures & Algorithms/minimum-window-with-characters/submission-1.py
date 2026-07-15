class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        target_freq  = Counter(t)
        window_freq = {}

        required = len(target_freq)
        formed = 0

        left = 0

        ans = (float("inf"), 0, 0)

        for right in range(len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1
            
            # Check if current character satisfies its required frequency
            if s[right] in target_freq and window_freq[s[right]] == target_freq[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)

                window_freq[s[left]] -= 1
                
                if (
                    s[left] in target_freq
                    and window_freq[s[left]] < target_freq[s[left]]
                ):
                    formed -= 1

                left += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
