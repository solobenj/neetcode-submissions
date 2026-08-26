class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        freq = []
        for i in range(0, len(nums)+1):
            freq.append([])


        for n, c in counts.items():
            freq[c].append(n)

        res = []
        for f in reversed(freq):
            for n in f: 
                res.append(n)
                if len(res) >= k: return res
        return res