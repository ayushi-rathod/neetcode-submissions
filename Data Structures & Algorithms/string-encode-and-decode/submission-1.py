class Solution:

    def encode(self, strs: List[str]) -> str:
        finalStr = ""
        for s in strs:
            finalStr = finalStr + str(len(s)) +"#"+ s 
        print(finalStr)
        return finalStr


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim = s.find("#",i)
            length = int(s[i:delim])

            newStr = s[delim+1:delim+1+length]

            i = delim + 1+ length
            res.append(newStr)
        
        return res