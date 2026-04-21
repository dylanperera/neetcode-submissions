from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Option 1: Create two hashtables to store the count of each character in the array and then compare the two to see if they are equal
            # Time -> 3n = O(n)
            # Space -> n + n = 2n = O(n)

        # Option 2: 
            # Check if same length
            # Create one hashtable of the counts for s, go through t, decrease the count of the character when we see it
            # go through table and check if all values are 0
            # Time -> n + n + n = 3n = O(n)
            # Space -> n = O(n)

        counts = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for ch in s:
            counts[ch] += 1
        
        for ch in t:
            counts[ch] -= 1

        for key,value in counts.items():
            if value != 0:
                return False

        return True
