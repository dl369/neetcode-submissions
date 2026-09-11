class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indexMap;
        
        for (auto it = nums.begin(); it != nums.end(); ++it) {
            int comp = target - *it;
            int index = it - nums.begin();

            if (indexMap.contains(comp)) {
                return {indexMap[comp], index};
            }

            indexMap.insert({*it, index});
        }

        return {};
    }
};
