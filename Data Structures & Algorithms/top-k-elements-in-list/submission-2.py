class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for n in nums:
            hmap[n] = hmap.get(n, 0)+1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for i, c in hmap.items():
            bucket[c].append(i)
        
        ans = []
        for i in range(len(bucket)-1, -1, -1):
            if (k == 0):
                return ans
            if len(bucket[i]) > 0:
                for num in bucket[i]:
                    ans.append(num)
                    k -=1
                    if k == 0: return ans
        return ans
        