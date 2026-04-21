from collections import defaultdict
class Solution:
    # Top k most frequent elements
    # First we need to find the frequency of each element -> n * log(n): {1: 1, 3: 4, 2: 5, 4: 4}
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = defaultdict(int)
        
        for num in nums:
            freq_counter[num] += 1

        largest_freq = 0
        for value in freq_counter.values():
            largest_freq = max(largest_freq, value)

        bucket = [[] for _ in range(largest_freq)]
        
        for key,value in freq_counter.items():
            bucket[value-1].append(key)


        k_ptr = len(bucket) - 1
        k_counter = k
        result = []
        while k_counter > 0:
            if len(bucket[k_ptr]) > 0:
                result.append(bucket[k_ptr].pop())
                k_counter -= 1
            else:
                k_ptr -= 1
        

        return result
