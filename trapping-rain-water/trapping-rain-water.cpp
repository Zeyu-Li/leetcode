class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int min_height = 0;
        int volume = 0;
        int pastHeight = 0;
        
        while (left < right) {
            // if it does not meet the requirements of min, increment
            // in the right direction
            if (!(height[left] > min_height)) {
                left++;
                continue;
            }
            if (!(height[right] > min_height)) {
                right--;
                continue;
            }
            
            // somehow need debugging
            // find volume layer by layer
            min_height = min(height[left], height[right]);
            // cout << "min: " << min_height << endl;
            int tmpL = left + 1;
            while (tmpL < right) {
                // if 
                if (min_height-height[tmpL] > 0) {
                    // forget past height so we don't need to double count
                    // cout << (min_height-pastHeight-height[tmpL]) << endl;
                    if (height[tmpL] <= pastHeight)
                        volume+=min_height-pastHeight;
                    else 
                        volume+=min_height-height[tmpL];
                }
                    
                tmpL++;
            }
            pastHeight = min_height;
            
        }
        
        return volume;
    }
};