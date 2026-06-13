from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Need to loop over nums and check if we have seen target - nums[curr index]
        # If not, we add the (value, index) pair
        # The reason we store the index is because we need to return the indicies of the values that sum to the target
        seen = defaultdict(int)

        for index, value in enumerate(nums):
            if (target - value) in seen:
                return [seen[target - value], index]
            elif value not in seen:
                seen[value] = index
