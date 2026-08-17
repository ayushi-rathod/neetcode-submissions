class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = {}
        for i in s:
            smap[i] = smap.get(i, 0) + 1

        for j in t:
            if j not in smap:
                return False
            smap[j] = smap.get(j) -1
            
        return all(val == 0 for val in smap.values())        