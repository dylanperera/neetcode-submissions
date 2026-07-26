from collections import defaultdict
class Solution:
    # Input: a string s
    # Output: Length of longest substring with no repeating characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Since we're looking for a sub-array and have a constraint metric (max substring)
        # We can apply sliding window technique with a hash-table to keep track of what/how many characters in a substring
        count = defaultdict(int)
        left = 0
        currMaxLength = 0

        for right in range(0, len(s)):
            count[s[right]] += 1

            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            currMaxLength = max(right - left + 1, currMaxLength) 

        return currMaxLength