from collections import defaultdict
class Solution:
    # Given an array of numbers and an integer k
    # Find if there are two distinct indicies i and j in the array such that they pass the condition mentioned
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k <= 0:
            return False
        # initialize left ptr = 0
        leftPtr = 0

        values_seen = defaultdict(int)
        values_seen[nums[leftPtr]] = 1

        # have a for loop where rightptr is the index (starts from 1 to end of array)
        for rightPtr in range(1, len(nums)):
            values_seen[nums[rightPtr]] += 1
            # while my sub-array size > k:
            while rightPtr - leftPtr > k:
                # move the left pointer up
                values_seen[nums[leftPtr]] -= 1
                leftPtr += 1
                

            # compare the right point to the left point
            if values_seen[nums[rightPtr]] > 1:
                # return true if equal
                return True

        # return false
        return False


        
