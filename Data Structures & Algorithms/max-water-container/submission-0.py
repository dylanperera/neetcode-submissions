class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # We're always doing width * height
        # Starting from the ends gives maximum width
        # The smaller end moves in

        leftPtr = 0
        rightPtr = len(heights) - 1
        maxProduct = 0
        currProduct = 0

        while leftPtr < rightPtr:
            minBar = min(heights[leftPtr], heights[rightPtr])
            currProduct = minBar * (rightPtr - leftPtr)

            maxProduct = max(maxProduct, currProduct)

            if heights[leftPtr] <= heights[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1

        return maxProduct
