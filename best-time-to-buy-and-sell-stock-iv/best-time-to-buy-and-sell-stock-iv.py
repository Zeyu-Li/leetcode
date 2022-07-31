class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0: return 0
        
        pLen = len(prices)
        dp = [[0 for _ in range(pLen)] for _ in range(k+1)]
        
        for i in range(1, k + 1):
            prev = dp[i-1][0] - prices[0]
            for j in range(1, pLen):
                dp[i][j] = max(dp[i][j-1], prev + prices[j])
                prev = max(prev, dp[i-1][j] - prices[j])
            
        return dp[-1][-1]
        