class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)

        for s in strs:
            bucket = [0]*26

            for i in range(len(s)):
                count = ord(s[i]) - ord('a')
                bucket[count] += 1

            hmap[tuple(bucket)].append(s)
        
        return list(hmap.values())