from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(s):
            if len(s) == 0:
                return 1
            
            if s[0] == "0":
                return 0
            
            if len(s) == 1:
                return 1
            
            if s[1] == "0" and int(s[0]) <= 2:
                return dfs(s[2:])
            elif int(s[0:2]) > 26 or int(s[0]) > 2:
                return dfs(s[1:])
            else:
                return dfs(s[1:]) + dfs(s[2:])

        return dfs(s)