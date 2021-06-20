class Solution {
public:
    int minPartitions(string n) {
        auto it = max_element(begin(n), end(n));
        return (*it) - '0';
    }
};