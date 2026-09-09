class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            n = i + ((j-i) // 2)
            if nums[n] == target:
                return n
            elif nums[n] > target:
                j = n - 1
            elif nums[n] < target:
                i = n + 1
        return -1

