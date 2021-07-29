class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<pair<int, int>> zeros;
        // get zeros
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    zeros.push_back(make_pair(j, i));
                }
            }
        }
        
        unordered_set<int> columns;
        unordered_set<int> rows;
        
        for (auto pairs : zeros) {
            rows.insert(pairs.first);
            columns.insert(pairs.second);
        }
        
        // set zeros
        for (auto row : rows) {
            for (int i = 0; i < matrix.size(); i++) {
                matrix[i][row] = 0;
            }
        }
        for (auto column : columns) {
            for (int i = 0; i < matrix[0].size(); i++) {
                matrix[column][i] = 0;
            }
        }
    }
};