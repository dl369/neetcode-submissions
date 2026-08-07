class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for i, num in enumerate(nums):
            
            diff = target - num

            if diff in comp:
                return [comp[diff], i]
            
            comp[num] = i 