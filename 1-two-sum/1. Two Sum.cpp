class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, int> mpp;

        for (int i = 0; i < nums.size(); i++){
            int goal = target - nums[i];

            if (mpp.find(goal) != mpp.end()){
                return {mpp[goal], i};
            }
            mpp[nums[i]] = i;
        }
        return {};
        
    }
};