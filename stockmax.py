def stockmax(prices):
    dp = [0] * (len(prices) + 1)
    max_ar = 0
    
    for i in range(len(prices) - 1, -1, -1):
        max_ar = max(max_ar, prices[i])
        dp[i] = max(dp[i + 1], max_ar - prices[i]+dp[i+1])
    
    return dp[0]