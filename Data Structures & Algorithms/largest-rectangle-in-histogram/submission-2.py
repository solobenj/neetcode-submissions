class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxres = 0
        stack = [] # (start, h)

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                topi, toph = stack.pop()
                w = i - topi
                maxres = max(maxres, w * toph)
                start = topi

            stack.append((start, h))
        
        while stack:
            topi, toph = stack.pop()
            maxres = max(maxres, toph * (len(heights) - topi))
            
        return maxres