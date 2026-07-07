from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            # Base case: successfully decoded the entire string
            if i == len(s):
                return 1
            
            # Base case: single '0' cannot be decoded
            if s[i] == "0":
                return 0
            
            # Decision 1: Decode a single digit
            res = dfs(i + 1)
            
            # Decision 2: Decode two digits (must be between "10" and "26")
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
                res += dfs(i + 2)
                
            return res

        return dfs(0)