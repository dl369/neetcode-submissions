class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2

            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target is in the left sorted half
                else:
                    l = mid + 1  # Target is in the right half
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target is in the right sorted half
                else:
                    r = mid - 1  # Target is in the left half
        
        return -1
