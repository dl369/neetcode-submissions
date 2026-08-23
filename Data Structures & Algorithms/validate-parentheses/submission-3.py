class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        
        stack = []

        for c in s:            
            brackets = {"]":"[", ")":"(", "}":"{"}
            
            if c in brackets.values():
                stack.append(c)
            elif stack:
                openBrack = stack.pop()
                if brackets[c] != openBrack:
                    return False
            else:
                return False
        
        return False if stack else True
