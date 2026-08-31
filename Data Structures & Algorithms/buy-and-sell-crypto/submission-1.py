class Solution:
    # Input: prices of a stock on a certain day 
    # Output: max profit we can make by buying and selling a coin
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window technique
        leftPtr = 0
        lenPrices = len(prices)
        maxProfit = 0
        # for loop
        for rightPtr in range(0, lenPrices):
            # while the leftPtr value is greater than the current stock price:
            while prices[leftPtr] > prices[rightPtr]: 
                # move the leftPtr up
                leftPtr += 1

            # compare the rightPtr stock price with the leftPtr stock price
            maxProfit = max(maxProfit, prices[rightPtr] - prices[leftPtr])

        return maxProfit
