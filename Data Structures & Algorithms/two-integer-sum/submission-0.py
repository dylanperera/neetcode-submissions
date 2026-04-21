from collections import defaultdict
class Solution:
    # The idea is to check if two values in the array sum to the target (must be two different indicies)
    # Check if target minus current value exists in the hash-table (store value, index)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = defaultdict(int)

        for i in range(0, len(nums)):
            value_to_check = target - nums[i]

            if value_to_check in value_index:
                return [value_index[target - nums[i]], i]
            else:
                value_index[nums[i]] = i

