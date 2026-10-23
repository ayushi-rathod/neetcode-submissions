class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_count = 0
        for n in hset:
            length= 0
            if n-1 not in hset:
                while n+length in hset:
                    length+=1
                max_count = max(max_count, length)
        return max_count
        