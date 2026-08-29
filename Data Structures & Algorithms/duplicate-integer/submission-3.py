class Solution:
    # Input: Nums -> integer array
    # Output: If any value appears more than once -> True otherwise false
    
    # Test cases:
    # 1. [1,2,3,3] -> True
    # 2. [] -> False
    # 3. [1] -> False
    # 4. [1, 1, 1, 1, 2] -> True
    # 5. [1, 2, 3, 1, 2] -> True


    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize set   
        seen = set()

        # Loop through nums
        for num in nums:
            # if the current number being analyzed exists in set, return true
            if num in seen:
                return True
            # else add the value to set
            else:
                seen.add(num)

        
        # return false
        return False
        
        