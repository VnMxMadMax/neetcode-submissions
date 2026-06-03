class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {char: s1.count(char) for char in set(s1)}

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            window = s2[l:r+1]
            window_freq = {char: window.count(char) for char in set(window)}

            if window_freq == s1_freq:
                return True

            l += 1
            r += 1

        return False