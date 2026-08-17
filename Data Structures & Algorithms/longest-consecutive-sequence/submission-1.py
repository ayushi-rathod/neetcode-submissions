class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        max_count = 0
        for num in hset:
            length = 0
            if (num-1) not in hset:
                while (num +length) in hset:
                    length += 1
                max_count = max(max_count, length)
        return max_count