class Solution:
    # Input: a list of numbers in random order, number can be small, large, or 0 (see constraints)
    # Output: Longest sequence of numbers where the next value is greater than the current value by 1

    def longestConsecutive(self, nums: List[int]) -> int:
        # [2, 20, 6, 10, 3, 4, 5, 21, 22]

        # Brute force solution -> Sort elements, then apply sliding window: O(n log n)
        
        # Turning the input into a set would get rid of duplicates and allow look-ups
        vals = set(nums)

        # Find all the starting points and put into an array
        starting_points = []

        for num in vals:
            if (num-1) not in vals:
                starting_points.append(num)
        
        # Loop over this array:
        longest_seq = 0
        for sp in starting_points:
            # for each value in the array, going to continuously check if the next value exists in the set
            curr_seq = 0
            curr_val = sp
            while True:
                curr_seq += 1
                if curr_val+1 not in vals:
                    break
                curr_val += 1
            longest_seq = max(longest_seq, curr_seq)


        return longest_seq
        
