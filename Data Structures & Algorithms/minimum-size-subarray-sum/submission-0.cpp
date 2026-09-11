class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int currSum = 0;
        int minLen = INT_MAX; 

        for (int r = 0; r < static_cast<int>(nums.size()); ++r) {
            currSum += nums[r];

            while (currSum >= target) {
                minLen = std::min(minLen, r - l + 1); // Comparing int with int
                currSum -= nums[l];
                l++; // Fixed: Increment left pointer to shrink the window
            }
        }

        // Return 0 if no valid subarray was found, otherwise return minLen
        return (minLen == INT_MAX) ? 0 : minLen;
    }
};