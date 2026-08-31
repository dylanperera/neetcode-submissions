class Solution:
    # Given an array of numbers, remove the duplicates
    # The first k numbers should non-duplicated numbers

    # seen = [1,2,3,4]
    # [1,1,1,2,3,4]
    # [1,2,3,4,1,1]
    # []
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize a set of values we've seen
        duplicates_removed_set = [nums[0]]
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                duplicates_removed_set.append(nums[i])

        for i in range(0, len(duplicates_removed_set)):
            nums[i] = duplicates_removed_set[i]

        return len(duplicates_removed_set)

            
