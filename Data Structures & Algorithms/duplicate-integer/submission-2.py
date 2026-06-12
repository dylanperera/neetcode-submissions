class Solution:
    # Input: List of numbers
    # Ouput: Boolean determining if there is 2 or more of a value
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Have a set to store the values as we see them
        values = set()

        for num in nums:
            if num in values:
                return True
            else:
                values.add(num)

        return False
        
        