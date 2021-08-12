class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = INT_MAX;
        
        // sort
        sort(nums.begin(), nums.end());
            
        for (int i = 0; i < nums.size() && closest != 0; i++) {
            // consider next number
            int low = i+1;
            int high = nums.size()-1;

            while (low < high) {
                int sum = nums[i] + nums[low] + nums[high];
                if (abs(target - sum) < abs(closest)) {
                    // we have found one canadate 
                    closest = target - sum;
                } 
                if (target > sum) {
                    low++;
                } else {
                    high--;
                }
            }
        }
        
        
        return target - closest;
    }
};