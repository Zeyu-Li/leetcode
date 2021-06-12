class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int finalSize = nums1.size() + nums2.size();
        bool even = finalSize % 2 == 0 ? true : false;
        
        int ptr1, ptr2, lastptr, mid, previous;
        ptr1 = ptr2 = mid = previous = 0;
        // floor division
        lastptr = finalSize / 2 + 1;
        // trival case
        if (nums1.size() == 0 && !even) { return nums2[lastptr-1]; }
        else if (nums2.size() == 0 && !even) { return nums1[lastptr-1]; }
        else if (nums1.size() == 0) { return ((double) nums2[lastptr-2] + nums2[lastptr-1]) / 2; }
        else if (nums2.size() == 0) { return ((double) nums1[lastptr-2] + nums1[lastptr-1]) / 2; }

        for (int i = 0; i < lastptr; i++) {
            previous = mid;
            if (ptr1 == nums1.size()) {
                mid = nums2[ptr2];
                ptr2++;
                continue;
            }
            
            if (ptr2 == nums2.size() || nums1[ptr1] < nums2[ptr2]) {
                mid = nums1[ptr1];
                ptr1++;
            } else {
                mid = nums2[ptr2];
                ptr2++;
            }
        }
        if (!even) {
            // cast to double
            return (double) mid;
        } else {
            return ((double) previous + mid) / 2;
        }
    }
};