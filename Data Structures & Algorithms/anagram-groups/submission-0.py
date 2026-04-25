from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))  # canonical form
            groups[key].append(word)
        
        return list(groups.values())