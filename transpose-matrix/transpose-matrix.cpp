class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
//         for (int i = 0; i < matrix.size(); i++) {
//             for (int j = i + 1; j < matrix[0].size(); j++) {
                
//             }
//         }
        vector<vector<int>> result;
        for (int i = 0; i < matrix[0].size(); i++) {
            vector<int> row;
            for (int j = 0; j < matrix.size(); j++) {
                row.push_back(matrix[j][i]);
            }
            result.push_back(row);
        }
        return result;
    }
};