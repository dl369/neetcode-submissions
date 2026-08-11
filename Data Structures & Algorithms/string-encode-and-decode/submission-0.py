import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        
        for s in strs:
            output += str(len(s)) + '#' + s
        
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        
        i = 0
        while i < len(s):
            m = re.match(r"(\d+)#", s[i:])
            length = m.group(1)

            i += len(length) + 1
            
            string = s[i:i+int(length)]

            output.append(string)
            
            i += int(length)

        return output
            
