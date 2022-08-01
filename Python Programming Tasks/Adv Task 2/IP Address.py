class Solution:
    def defangIPaddr(self, address: str) -> str:
        b=[]
        for i in address.split("."):
            b.append(i)
        output=b[0]+"[.]"+b[1]+"[.]"+b[2]+"[.]"+b[3]
        return output
        