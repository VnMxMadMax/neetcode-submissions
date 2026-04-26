from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            chars = list(word)     # convert string to list
            chars.sort()           # sort characters
            key = "".join(chars)   # convert back to string

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())