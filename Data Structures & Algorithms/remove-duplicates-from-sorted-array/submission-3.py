class Solution:
    # Given an array of numbers, remove the duplicates
    # The first k numbers should non-duplicated numbers

    # seen = [1,2,3,4]
    # [1,1,1,2,3,4]
    # [1,2,3,4,1,1]
    # []
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize a set of values we've seen
        seen = set()
        result = len(nums)
        # loop through the input nums
        for i in range(0, len(nums)-1):
            # if we've seen the input:
            if nums[i] in seen:
                # send another point to find another value for which we have not seen
                ptr2 = i+1
                swapped = False
                while ptr2 < len(nums) and swapped == False:
                    if nums[ptr2] not in seen:
                        temp = nums[i]
                        nums[i] = nums[ptr2]
                        nums[ptr2] = temp
                        swapped = True

                    ptr2 += 1

            seen.add(nums[i])

        seen = set()
        for i in range(0, len(nums)):
            if nums[i] in seen:
                return i
            else:
                seen.add(nums[i])

        return len(nums)

            
