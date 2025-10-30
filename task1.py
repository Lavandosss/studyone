def cut_rod(n, prices):
    dp = [0] * (n + 1)        
    cuts = [[] for _ in range(n + 1)]  

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j <= len(prices):
                if dp[i] < prices[j - 1] + dp[i - j]:
                    dp[i] = prices[j - 1] + dp[i - j]
                    cuts[i] = cuts[i - j] + [j]
    return dp[n], cuts[n]
n = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]
value, lengths = cut_rod(n, prices)
print("Max profit:", value)
print("Length:", lengths)
