class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxres = 0
        n = len(heights)
        stack = []

        for i in range(0, n):
            start = i 
            while stack and i < n and heights[i] < stack[-1][1]:
                top, h = stack.pop()
                w = i - top
                #print(" Pop!", top, w, h)
                maxres = max(maxres, w * h)
                start = top
            
            stack.append((start, heights[i]))
            #print(i, start, stack)

        #print(stack)
        while stack:
            top, h = stack.pop()
            w = n - top
            #print(top, w, h)
            maxres = max(maxres, w * h)

        return maxres