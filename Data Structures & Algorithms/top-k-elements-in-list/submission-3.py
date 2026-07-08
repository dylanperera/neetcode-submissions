from collections import defaultdict
class Solution:

    # Return the k most frequent elements within the array

    # [1,2,2,3,3,3], k = 2 -> 2,3

    # Get the frequency of each number using a hashtable
    # Create an array of len(nums) to represent the most amount of times a number can appear
    # This will be an array of arrays. The inner array will contain elements with that specific frequemcy
    # Loop backwards from the outter array getting the k most elements

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            freq_counter[num] += 1
        
        for key,value in freq_counter.items():
            bucket[value].append(key)

        for i in reversed(bucket):
            for j in i:
                if len(result) == k:
                    return result
                else:
                    result.append(j)
        
        return result
    
        