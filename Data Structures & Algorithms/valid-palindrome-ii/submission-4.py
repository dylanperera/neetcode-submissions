class Solution:
    # Input: string of lowercase characters
    # Output: boolean determining whether we have a valid palindrome or not

    # abbda

    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        # have two pointers, one at beginning of s and one at the end
        leftPtr = 0
        rightPtr = len(s) - 1

        # have a bool to represent whether we've deleted or not -> can only delete once
        deleted_once = False
        
        # while the pointers dont cross or touch:
        while leftPtr < rightPtr:
            # if the pointers values are not equal:
            if s[leftPtr] != s[rightPtr]:
                if deleted_once == True:
                    return False
                # otherwise:
                else:
                    deleted_once = True
                    # Consider removing the rightPtr element, will the rest result in a palindrome?
                    if s[leftPtr:rightPtr][::-1] == s[leftPtr:rightPtr]:
                        return True
                    elif s[leftPtr+1:rightPtr+1][::-1] == s[leftPtr+1:rightPtr+1]:
                        return True
                    else:
                        return False
            # move both inwards 
            else:
                leftPtr += 1
                rightPtr -= 1

        return True
        