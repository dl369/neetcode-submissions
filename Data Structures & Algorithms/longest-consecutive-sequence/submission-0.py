class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for num in nums:
            if num - 1 not in s:
                currLen = 1
                currNum = num + 1

                while currNum in s:
                    currLen += 1
                    currNum += 1
                
                if currLen > longest:
                    longest = currLen
        
        return longest
