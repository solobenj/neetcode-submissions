class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroes = 0
        for i in nums:
            if i != 0: prod *= i
            else: 
                zeroes += 1
        
        if zeroes > 1: return [0]*len(nums)

        res = [None]*len(nums)
        for idx, i in enumerate(nums):
            if zeroes == 1:
                if i == 0:
                    res[idx] = prod
                else:
                    res[idx] = 0
            else:
                res[idx] = (prod // i)
        return res


            


