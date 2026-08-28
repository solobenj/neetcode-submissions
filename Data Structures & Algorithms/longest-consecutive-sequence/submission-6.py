class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if num in mp and mp[num] != 0: continue

            mp[num] = mp[num - 1] + mp[num + 1] + 1
            mp[num - mp[num-1]] = mp[num]
            mp[num + mp[num+1]] = mp[num]
            res = max(res, mp[num])
        return res
