class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for i in range(len(nums)):
            
            diff = target - nums[i]

            if diff in comp:
                return sorted([i, comp[diff]])
            
            comp[nums[i]] = i 