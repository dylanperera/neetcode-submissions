class Solution:
    # Inputs: 1. Array of numbers, 2. Value to remove from numbers array
    # Output: Number of elements which are not equal to val

    # numbers= [1,2,3,4,2,4,5,3] and val = 3
    # numbers = [1,2,4,2,4,5,_,_] 

    # [3, 2, 2, 3]
    # [2, 3, 2, 3]

    def removeElement(self, nums: List[int], val: int) -> int:
        num_elements = len(nums)
        num_vals = num_elements
        # loop through all elements of nums
        for i, num in enumerate(nums):
            # if the current value is equal to val, find the next available value that is not the value to remove and swap
            if num == val and i is not (num_elements - 1):
                for j in range(i+1, num_elements):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break

        # Find where the first occurence of val is in nums

        for i, num in enumerate(nums):
            if num == val:
                num_vals = i
                break

        return num_vals

        

