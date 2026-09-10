class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int l = 0;
        int r = 0;
        std::set<char> charSet;
        int maxLen = 0;

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
