class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        a = sorted(s)
        b = sorted(t)
        i = 0
        while i < len(s):
            if a[i] != b[i]: return False
            i += 1
        return True
        
        