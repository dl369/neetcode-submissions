class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        size_t l = 0;
        size_t r = 0;
        std::unordered_set<char> charSet;
        size_t maxLen = 0;

        while (r < s.size()) {
            while (charSet.contains(s[r])) {
                charSet.erase(s[l]);
                l++;
            }

            charSet.insert(s[r]);
            maxLen = std::max(maxLen, r - l + 1);
            r++;
        }

        return maxLen;
    }
};
