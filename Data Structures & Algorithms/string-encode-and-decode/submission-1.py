class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            for c in s:
                encoded += format(ord(c), '08b')
            encoded += ";"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        #print(s)

        current_str = ""
        current_chr = ""
        for idx, ns in enumerate(s):
            
            if ns == ";":
                decoded.append(current_str)
                current_str = ""
                current_chr = ""
            else:
                current_chr += ns

            if len(current_chr) >= 8:
                current_str += chr(int(current_chr, 2))
                current_chr = ""
            
            #print(idx, ns, current_chr, current_str)

        return decoded