class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_dict = {}
        max_freq = 0
        max_window_size = 0

        for r in range(len(s)):
            freq_dict[s[r]] = freq_dict.get(s[r], 0) + 1

            # Track highest frequency character in current window
            max_freq = max(max_freq, freq_dict[s[r]])

            window_size = r - l + 1

            # If replacements needed exceed k, shrink window
            if window_size - max_freq > k:
                freq_dict[s[l]] -= 1
                l += 1

            max_window_size = max(max_window_size, r - l + 1)

        return max_window_size