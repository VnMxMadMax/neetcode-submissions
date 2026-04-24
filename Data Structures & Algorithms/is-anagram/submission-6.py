class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        if slist == tlist:
            return True
        else:
            return False
        