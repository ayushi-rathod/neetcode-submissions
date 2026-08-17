class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        max_area = 0
        curr_max = 0

        while (left < right):
            curr_max = (right - left) * min(heights[right], heights[left])
            
            max_area = max(max_area, curr_max)
            if (heights[left] > heights[right]):
                right = right -1
            else:
                left = left+1
        return max_area