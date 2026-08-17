class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hmap:
                return [hmap.get(compliment), i]
            hmap[nums[i]] = i
        
        return []