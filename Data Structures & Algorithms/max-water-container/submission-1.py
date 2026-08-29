class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            res = max(res, area)

            # move the lower one, as
            # storage capacity is always limited by how high
            # the lower one is
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res