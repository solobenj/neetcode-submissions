class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        c = len(nums)
        i = 0
        j = c - 1
        
        while i < c and j >= 0 and i != j:
            sum = nums[i] + nums[j]
            if sum == target: return [i, j]
            elif sum < target:
                i += 1
            elif sum > target:
                j -= 1

            
        return []