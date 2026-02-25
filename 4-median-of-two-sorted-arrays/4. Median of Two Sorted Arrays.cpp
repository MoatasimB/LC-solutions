class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        int n1 = nums1.size();
        int n2 = nums2.size();

        if(n2 < n1){
            return findMedianSortedArrays(nums2, nums1);
        }

        int total = n1 + n2;

        int half = (total / 2);

        int l = 0;
        int r = n1;

        while (l <= r){
            int midA = (l + r) / 2;
            int midB = half - midA;

            int leftA = midA - 1 >= 0 ? nums1[midA - 1] : INT_MIN;
            int rightA = midA < n1 ? nums1[midA] : INT_MAX;
            int leftB = midB - 1 >= 0 ? nums2[midB - 1] : INT_MIN;
            int rightB = midB < n2 ? nums2[midB] : INT_MAX;

            if (leftA <= rightB && leftB <= rightA){
                if (total % 2 == 0){
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0;
                }
                return min(rightA, rightB);

            }
            else if (leftA > rightB){
                r = midA - 1;
            }
            else{
                l = midA + 1;
            }
        }
        
        return 0.0;
    };
};