// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        // trivally similar to search insert position
        int top, mid, bottom;
        top = n-1;
        bottom = 0;
        while (bottom <= top) {
            mid = bottom + (top-bottom) / 2;
            if (!isBadVersion(mid)) {
                bottom = mid+1; 
            } else {
                top = mid-1;
            }
        }
        
        return bottom;
    }
};