class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = [0]* n
        left_arr[0] = 1
        right_arr = [0]* n
        right_arr[-1] = 1

        for i in range(1,len(nums)):
            left_arr[i] = nums[i-1] * left_arr[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]

        res = [0]*n
        for i in range(len(nums)):
            res[i] = left_arr[i] * right_arr[i]

        return res