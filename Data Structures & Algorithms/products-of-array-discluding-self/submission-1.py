class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        left = [0]*len(nums)
        right = [0]*len(nums)
        left[0] = 1
        right[-1] = 1
        n = len(nums)
        
        for i in range(1,len(nums)):
            left[i] = nums[i-1] * left[i-1]
            right[n-i-1] = nums[n-i] * right[n-i]

        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res