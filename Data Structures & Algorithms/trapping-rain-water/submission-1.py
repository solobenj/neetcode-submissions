class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = [0] * len(height)
        leftMax[0] = height[0]
        for i in range(1, len(height)-1):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0] * len(height)
        rightMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, 0, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        


        for idx, h in enumerate(height):
            water = min(leftMax[idx], rightMax[idx]) - h
            if water > 0:
                res += water

        return res