class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        l = 0
        r = 0
        minLen = math.inf
        minString = ""
        
        tCount = defaultdict(int)
        for c in t:
            tCount[c] += 1

        currMatches = 0
        reqMatches = len(tCount)

        while r < len(s):
            count[s[r]] += 1 

            if s[r] in tCount and count[s[r]] == tCount[s[r]]:
                currMatches += 1

            while currMatches == reqMatches:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    minString = s[l:r + 1]
                    
                count[s[l]] -= 1
                if count[s[l]] < tCount[s[l]]:
                    currMatches -= 1
                l += 1
            r += 1

      
        return minString
            
                