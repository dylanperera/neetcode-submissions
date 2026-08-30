class Solution:
    # Input: a list of characters/strings to swap (reverse them)
    # Output: nothing, the list must be reversed in-place
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return 

        # Initialize two pointers
        leftPtr = 0
        rightPtr = len(s) - 1

        # while leftPtr < rightPtr, swap the characters
        while leftPtr < rightPtr:
            temp = s[leftPtr]
            s[leftPtr] = s[rightPtr]
            s[rightPtr] = temp

            leftPtr += 1
            rightPtr -= 1            