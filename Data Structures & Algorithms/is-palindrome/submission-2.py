class Solution:
    # Input: string s
    # Output: boolean which represents whether a string reads the same forward and backwards

    # Key consideration:
    # 1. Ignore non-alphanumeric characters (A-Z, a-z, 0-9)
    # Test cases:
    # 1. s = "hello world" -> False
    # 2. s = "i was 1 ! ? saw i" -> True
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        s = s.lower()

        # using two pointer technique, have two pointers start at beginning and end of the input
        leftPtr = 0
        rightPtr = len(s) - 1

        # while the pointers have not crossed or met, continue doing the following:
        while leftPtr < rightPtr:
            # while the left pointers character is not alphanumeric and less than right pointer, move forward
            while self.isAlphaNumeric(s[leftPtr]) == False and leftPtr < rightPtr:
                leftPtr += 1

            # while the right pointers character is not alphanumeric and greater than the left pointer, move backwards
            while self.isAlphaNumeric(s[rightPtr]) == False and rightPtr > leftPtr:
                rightPtr -= 1

            # if the values of the pointers are equal to each other move each pointer
            if s[leftPtr] == s[rightPtr]:
                leftPtr += 1
                rightPtr -= 1
            # otherwise return false - not a valid palindrome
            else:
                return False

        return True
    
    def isAlphaNumeric(self, ch: str) -> bool:
        # check if character is between A-Z or a-z or 0-9
        if (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9'):
            return True

        return False
        