from collections import defaultdict
class Solution:
    # Need to check if a value appears more than once
    # Go through all the values and check if a value appears more than once
    # If the value appears more than once, we return true
    # To store the count of values, we will use a hashtable

    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict()

        for num in nums:
            if num in count:
                return True
            else:
                count[num] = 1

        return False