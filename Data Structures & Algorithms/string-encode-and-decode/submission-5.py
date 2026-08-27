class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s: return []

        res = []
        idx = 0
        while idx < len(s):
            j = idx
            while s[j] != '#':
                j += 1
            sz = int(s[idx:j])
            idx = j + 1
            res.append(s[idx:idx + sz])
            idx += sz
        return res

             
