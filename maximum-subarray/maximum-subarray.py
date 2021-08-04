class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp solution
        _max = nums[0]
        current_canadiate = _max
        
        for i in range(1, len(nums)):
            current_canadiate = max(nums[i], current_canadiate+nums[i])
            _max = max(_max, current_canadiate)
            
        return _max
        
# cpp brute force solution:
# class Solution {
# public:
#     int maxSubArray(vector<int>& nums) {
#         int max = INT_MIN;
#         for (int i = 0; i < nums.size(); i++) {
#             for (int j = i; j < nums.size(); j++) {
#                 int total = 0;
#                 for (int k = i; k < j+1; k++) {
#                     total += nums[k];
#                 }
#                 if (total > max) {
#                     max = total;
#                 }
#             }
#         }
        
#         return max;
#     }
# };