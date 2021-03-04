// is not optimal solution
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        bool flag = true;
        if (nums1.size()>nums2.size()) {
            // move nums2 to nums1
            for (auto it : nums2) {
                nums1.push_back(it);
                sort(nums1.begin(), nums1.end());
            }
        } else {
            flag = false;
            // move nums1 to nums2
            for (auto it : nums1) {
                nums2.push_back(it);
                sort(nums2.begin(), nums2.end());
            }
        }
        
        if (flag) {
            int size = nums1.size();
            if (size%2) {
                // floor divides then returns middle casting to double
                return (double) nums1[size/2];
            } else {
                // average middle
                int first = size/2;
                return (double) (nums1[first]+nums1[first-1])/2.0;
            }
        } else {
            int size = nums2.size();
            if (size%2) {
                // floor divides then returns middle casting to double
                return (double) nums2[size/2];
            } else {
                // average middle
                int first = size/2;
                return (double) (nums2[first]+nums2[first-1])/2.0;
            }
        }
    }
};