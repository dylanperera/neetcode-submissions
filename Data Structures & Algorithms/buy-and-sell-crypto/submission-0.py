class Solution:
    # Input: List of prices for a stock over some period of time
    # Output: Maximum profit we can obtain by buying a stock and selling it later

    # [3, 3, 10, 20, 2, 4, 5, 30]

    def maxProfit(self, prices: List[int]) -> int:
        
        # We are essentially look for the best sub-array
        # This means we can apply sliding window method, where the sub-array is valid when the right edge is > left edge
        left = 0
        currMaxProfit = 0

        for right in range(0, len(prices)):
            while prices[right] < prices[left]:
                left += 1

            tempProfit = prices[right] - prices[left]
            currMaxProfit = max(currMaxProfit, tempProfit)

        return currMaxProfit