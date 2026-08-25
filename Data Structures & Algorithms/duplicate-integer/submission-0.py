class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        found = False
        last = math.inf
        for n in nums: 
            if last != math.inf and n == last: 
                found = True
                break
            last = n

        return found