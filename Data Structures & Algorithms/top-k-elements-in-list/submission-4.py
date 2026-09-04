class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        heap = []
        for n in nums:
            hmap[n] = hmap.get(n, 0)+1
        
        for key, freq in hmap.items():
            heapq.heappush(heap,(freq, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
