// brute force because I can't be bothered
class Solution {
public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        int count;
        vector<int> result;
        for (auto query : queries) {
            count = 0;
            for (auto point : points) {
                if ((point[0] - query[0]) * (point[0] - query[0]) + (point[1] - query[1]) * (point[1] - query[1]) <= query[2] * query[2]) count++;
            }
            result.push_back(count);
        }
        
        return result;
    }
};