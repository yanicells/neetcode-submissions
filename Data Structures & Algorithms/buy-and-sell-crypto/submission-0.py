class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ms = 0
        for i in range(len(prices)):
            for l in range(i, len(prices)):
                if i != l:
                    if (prices[l] - prices[i]) > ms:
                        ms = prices[l] - prices[i]
        return ms