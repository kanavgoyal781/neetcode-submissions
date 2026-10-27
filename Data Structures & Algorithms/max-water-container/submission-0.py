class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        area=0
        area_curr=0
        while left<right:
            area_curr=min(heights[left],heights[right])*(right-left)
            area=max(area,area_curr)
            if heights[right]>heights[left]:
                left=left+1
            else:
                right=right-1
        return area