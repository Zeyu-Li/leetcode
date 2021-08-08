class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // although dijkstra (or a bfs/dfs solution could work if you duplicate some branches) would work, DP is easier
        // for (int i = 0; i < triangle.size(); i++) {
        //     // for each layer
        //     for (int j = 0; j < triangle[i].size(); j++) {
        //         min
        //     }
        // }
        
        // bottom up is preferred solution :(
        
        // set up dp paths initalized with the bottom layer of the triangle
        vector<int> dp(triangle.back());
        
        for (int i = triangle.size()-2; 0 <= i; i--) {
            // for each item in row
            for (int j = 0; j <= i; j++) {
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j];
            }
        }
        
        return dp[0];
    }
};