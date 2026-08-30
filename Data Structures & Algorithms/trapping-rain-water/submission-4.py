class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        n = len(height) - 1
        l = 0
        r = n

        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, rightMax - height[r])

        return res