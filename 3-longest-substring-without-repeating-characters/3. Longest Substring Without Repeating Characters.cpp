class Solution {
public:
    int lengthOfLongestSubstring(string s) {

        unordered_map<char, int> mpp;

        int l = 0;
        int ans = 0;
        for (int r = 0; r < s.size(); r ++){
            if (mpp.find(s[r]) != mpp.end()){
                l = max(l, mpp[s[r]] + 1);
            }
            ans = max(ans, r - l + 1);
            mpp[s[r]] = r;

        }

        return ans;
        
    }
};