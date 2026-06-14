from collections import defaultdict
class Solution:
    # Input: List of numbers
    # Output: Element that appears the most amount of times
    def majorityElement(self, nums: List[int]) -> int:
        # have a frequency counter and get the value with the largest frequency
        freq_counter = defaultdict(int)

        majority_count = -math.inf
        majority_num = None

        for num in nums:
            freq_counter[num] += 1
            if freq_counter[num] > majority_count:
                majority_num = num
                majority_count = freq_counter[num]

        return majority_num