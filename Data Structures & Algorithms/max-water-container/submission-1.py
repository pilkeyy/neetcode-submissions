class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = float("-inf")
        while l < r:
            c_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, c_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
