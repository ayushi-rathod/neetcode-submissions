class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        hset = set()
        hset.add(s[0])
        left = 0
        right = 1
        count = 1
        max_count = 0

        while left < right and right < len(s):

            while s[right] in hset and left < right:
                hset.remove(s[left])
                left = left+1
                count -= 1
            
            hset.add(s[right])
            count += 1
            right += 1
            max_count = max(max_count, count)
        return max_count