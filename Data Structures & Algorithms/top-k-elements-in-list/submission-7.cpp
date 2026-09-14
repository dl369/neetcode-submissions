#include <ranges>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts;
        std::vector<vector<int>> freqs(nums.size() + 1);
        std::vector<int> res;

        for (const auto& num : nums) {
            counts[num]++;
        }

        for (const auto& [val, count] : counts) {
            freqs[count].push_back(val);
        }

        for (const auto& v : std::views::reverse(freqs)) {    
            for (const auto& num : v) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }

        return res;
    }
};
