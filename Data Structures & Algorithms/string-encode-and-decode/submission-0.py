class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # find the separator '#'
            j = i
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1:j+1+length]

            res.append(word)
            i = j+1+length

        return res
