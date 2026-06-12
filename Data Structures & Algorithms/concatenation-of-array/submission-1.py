class Solution:
    # The idea is to create an array that is essentially a concatenation of the input array
    # Input: One array
    # Output: The input array concatenated with itself
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Create the concatenation array
        nums_length = len(nums)

        concatenation = [0] * len(nums) * 2

        ptr1 = 0
        ptr2 = len(nums)

        while ptr1 < nums_length:
            concatenation[ptr1] = nums[ptr1]
            concatenation[ptr2] = nums[ptr1]

            ptr1 += 1
            ptr2 += 1

        return concatenation