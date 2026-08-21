class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        
        l = 0
        r = 0

        maxLen = 0
        maxFreq = 0
        while r < len(s):
            charCount[s[r]] += 1 
            maxFreq = max(maxFreq, charCount[s[r]])

            while l < r and r - l + 1 - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)

            r += 1
        
        return maxLen