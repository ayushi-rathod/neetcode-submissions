class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = 1
        right[-1] = 1
        p = [0]*n

        for i in range(1,len(left)):
            left[i] = nums[i-1]*left[i-1]
        
        for j in range(len(right)-2, -1, -1):
            right[j] = nums[j+1]*right[j+1]

        for k in range(len(left)):
            p[k] = left[k]*right[k]
        
        return p