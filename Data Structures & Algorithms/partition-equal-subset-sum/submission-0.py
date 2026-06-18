class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False

        target = total // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1):
            nextDP = set()

            for s in dp:
                if s + nums[i] == target:
                    return True
                
                nextDP.add(s + nums[i])
                nextDP.add(s)
            dp = nextDP
        
        return True if target in dp else False