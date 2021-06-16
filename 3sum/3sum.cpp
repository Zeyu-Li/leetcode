class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        
        // base cases
        if (nums.size() < 3) {
            return result;
        }
        
        // sort
        sort(nums.begin(), nums.end());
            
        for (int i = 0; i < nums.size() - 2; i++) {
            // check duplicates
            if (i == 0 || (i > 0 && nums[i] != nums[i-1])) {
                // consider next number
                int low = i+1;
                int high = nums.size()-1;
                
                // get two pair where sum = -nums[i]
                int sum = -nums[i];
                while (low < high) {
                    if (nums[low] + nums[high] == sum) {
                        // we have found one
                        vector<int> triplet;
                        triplet.push_back(-sum);
                        triplet.push_back(nums[low]);
                        triplet.push_back(nums[high]);
                        result.push_back(triplet);
                        // skip duplicates
                        while (low < high && nums[low] == nums[low+1])
                            low++;
                        while (low < high && nums[high] == nums[high-1])
                            high--;
                        low++;
                        high--;
                    } else if (nums[low] + nums[high] > sum) {
                        high--;
                    } else {
                        low++;
                    }
                }
            }
        }
        
        
        return result;
    }
};