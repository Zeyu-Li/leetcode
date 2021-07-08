class Solution {
public:
    // from https://leetcode.com/problems/count-primes/discuss/57594/My-easy-one-round-c%2B%2B-code
    int countPrimes(int n) {
        if (n <= 2) return 0;
        if (n == 3) return 1;
        
	    vector<bool> passed(n, false);
        
        int primes = 1;
        for (long i = 3; i < n; i+=2) {
            if (!passed[i]) {
                primes++;
                // avoid overflow
                if (n < i*i) continue;
                
                for (int j = i*i; j < n; j += i) {
                    passed[j] = true;
                }
            }
        }
        return primes;
    }
};