class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = {}

        for i in range(len(s)):
            if s[i] in hmap:
                hmap[s[i]] = hmap.get(s[i]) + 1
            else:
                hmap[s[i]] = 1
        
        for i in range(len(s)):
            if t[i] in hmap:
                hmap[t[i]] = hmap.get(t[i]) - 1
            else:
                hmap[t[i]] = 1

        
        for k,v in hmap.items():
            if v != 0:
                return False

        return True