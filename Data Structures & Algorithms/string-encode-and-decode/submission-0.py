class Solution:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        longStr = ""
        for s in strs:
            longStr = longStr + str(len(s)) + '#' + s
        return longStr

        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []
        i = 0
        
        while i < len(s):
            delim = s.find("#", i)
            length = int(s[i:delim])

            str_ = s[delim+1 : delim+1+length]
            decoded_str.append(str_)

            i = delim + 1 + length
        
        return decoded_str