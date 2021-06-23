class Solution {
public:
    double myPow(double x, int n) {
        if (n==0) return 1.0;
        else if (n < 0) return 1.0/(x*myPow(x, ~n));
        double result = 1;
            
        while (n > 1) {
            if (n % 2) {
                result *= x;
            }
            x*=x;
            // shift right by 1 (//2)
            n >>= 1;
        }
        return result * x;
    }
};