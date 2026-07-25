class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftPtr = 0
        rightPtr = len(s) - 1

        # Convert all characters to lower case
        s = s.lower()

        while leftPtr < rightPtr:
            while self.checkIfAlphanumeric(s[leftPtr]) == False and leftPtr < rightPtr:
                leftPtr += 1

            while self.checkIfAlphanumeric(s[rightPtr]) == False and rightPtr > leftPtr:
                rightPtr -= 1

            if s[leftPtr] != s[rightPtr]:
                return False

            leftPtr += 1
            rightPtr -= 1

        return True


    def checkIfAlphanumeric(self, char: str):
        if (char >= 'a' and char <= 'z') or char.isdigit() == True:
            return True
        else:
            return False

        