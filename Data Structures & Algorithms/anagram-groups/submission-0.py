class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in hmap:
                hmap[key].append(s)
            else:
                hmap[key] = [s]
        ans = []
        for val in hmap.values():
            ans.append(val)

        return ans
        