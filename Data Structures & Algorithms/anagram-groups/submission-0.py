class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {} # str -> str[]
        for s in strs:
            k = ''.join(sorted(s))
            if k in buckets:
                buckets[k].append(s)
            else:
                buckets[k] = [s]

        return list(buckets.values())
