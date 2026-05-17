import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        r = s[::-1]
        return s == r
        