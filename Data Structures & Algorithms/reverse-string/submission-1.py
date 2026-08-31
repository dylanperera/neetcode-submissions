class Solution:
    # Input: list of characters to reverse
    # Output: Nothing, modify the array in-place
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) <= 1:
            return 

        leftPtr = 0
        rightPtr = len(s) - 1

        while leftPtr < rightPtr:
            # swap the values
            temp = s[leftPtr]
            s[leftPtr] = s[rightPtr]
            s[rightPtr] = temp
            leftPtr+=1
            rightPtr-=1

        return
