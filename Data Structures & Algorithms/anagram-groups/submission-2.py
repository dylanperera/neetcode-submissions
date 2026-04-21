from collections import defaultdict
class Solution:
    # The idea is to group anagrams together
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list[str])

        # {{'h':1, 'a': 1, 't': 1}: ["hat"], {'a':1, 'c': 1, 't': 1}: ["act", "cat"], :["stop", "pots"]}
        # Go through all strings in strs -> O(n)
            # convert to hash table -> O(m) 
            # put into right 'bucket'
        for string in strs:
            sorted_arr = [0] * 26

            for ch in string:
                sorted_arr[ord(ch) % 26] += 1

                print(str(sorted_arr))
            
            groups[str(sorted_arr)].append(string)

        return list(groups.values())
