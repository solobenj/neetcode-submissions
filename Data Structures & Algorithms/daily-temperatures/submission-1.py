class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (temperature, index)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                top = stack.pop()
                res[top[1]] = i - top[1]
            stack.append([t, i])
        return res
