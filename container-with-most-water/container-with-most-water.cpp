class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0, end;
        end = height.size() - 1;
        int maxV = 0;
        
        while (start < end) {
            maxV = max(min(height[start], height[end]) * (end-start), maxV);
            if (height[start] < height[end])
                start++;
            else
                end--;
        }
        
        return maxV;
    }
};