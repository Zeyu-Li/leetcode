class Solution {
public:
    string convert(string s, int numRows) {
        
        if (numRows == 1) return s;
        
        vector<string> matrix(numRows);
        bool down = true;
        int currentRow = 0;
        for (int i = 0; i < s.size(); i++) {
            matrix[currentRow]+=s[i];

            if (currentRow + 1 == numRows) {
                down = false;
            } else if (currentRow == 0) {
                down = true;
            }
            if (down) {
                currentRow++;
            } else {
                currentRow--;
            }

        }
        // join back
        string finalStr;
        for (string str : matrix) {
            finalStr+=str;
        }
        return finalStr;
    }
};