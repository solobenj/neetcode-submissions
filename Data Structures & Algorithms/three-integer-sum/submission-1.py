class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, n in enumerate(nums):
            if n > 0: break
            if i > 0 and n == nums[i - 1]: continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                current = n + nums[l] + nums[r]
                if current > 0: 
                    r -= 1
                elif current < 0:
                    l += 1
                elif current == 0:
                    res.add((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            
        return list(res)