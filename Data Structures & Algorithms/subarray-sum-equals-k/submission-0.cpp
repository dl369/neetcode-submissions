class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> prefixSum;
        prefixSum[0] = 1;
        int currSum = 0;
        int count = 0;

        for (const auto& num : nums) {
            currSum += num;
            int diff = currSum - k;

            if (prefixSum.contains(diff)) {
                count += prefixSum[diff];
            }

            prefixSum[currSum] += 1;
        }

        return count;
    }
};