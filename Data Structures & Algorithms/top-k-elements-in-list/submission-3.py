class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in counts.items():
            freq[c].append(n)

        res = []
        for f in range(len(freq) - 1, 0, -1):
            for n in freq[f]: 
                res.append(n)
                if len(res) >= k: return res
        return res