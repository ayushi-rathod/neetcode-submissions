class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_sum = sum(nums)
        #  (n *(n+1)) // 2
        actual_sum = (len(nums) * (len(nums)+1))//2
        return actual_sum - num_sum