from collections import defaultdict

class Solution:
    # Input: two strings, s and t
    # Output: whether the strings 's' and 't' have the same characters and frequency

    # Test cases:
    # 1. s = "t", t = "qeweq" -> false
    # 2. s = "abc", t = "acc"
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of either strings are not equal, we can exit early and save computations
        if len(s) != len(t):
            return False

        # Get character count in input s using defaultdict
        count_s = defaultdict(int)

        for ch in s:
            count_s[ch] += 1

        # Loop through input t
        for ch in t:
            # if character in t does not exist in s_count: exit early
            if ch not in count_s:
                return False
            # if character in t does exist in s and is not 0: reduce count 
            if count_s[ch] != 0:
                count_s[ch] -= 1
            # else return false
            else:
                return False
    
        return True


        