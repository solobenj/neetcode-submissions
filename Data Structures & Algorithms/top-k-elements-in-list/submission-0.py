class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        pairs = [[k, v] for k, v in counts.items()]
        pairs = sorted(pairs, key = lambda x:x[1])
        
        res = []
        while len(res) < k:
            res.append(pairs.pop()[0])
        return res