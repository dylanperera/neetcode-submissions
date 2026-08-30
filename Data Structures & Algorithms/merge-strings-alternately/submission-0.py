class Solution:
    # Input: two strings (word1 and word2)
    # Output: merged string of word1 and word2
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merged string
        mergedString = []
        word1Length = len(word1)
        word2Length = len(word2)

        # one pointer at the beginning of word1
        ptr1 = 0
        # one pointer at the beginning of word2
        ptr2 = 0

        # while ptr1 < word1 length and ptr2 < word2 length:
        while ptr1 < word1Length and ptr2 < word2Length:
            # form the merged string
            mergedString.append(word1[ptr1])
            mergedString.append(word2[ptr2])
            ptr1+=1
            ptr2+=1

        # if ptr1 != word1 length:
        if ptr1 != word1Length:
            # attach the rest of the values from word1
            for i in range(ptr1, word1Length):
                mergedString.append(word1[i])
        # otherwise if ptr1 != word2 length:
        elif ptr2 != word2Length:
            for i in range(ptr2, word2Length):
                mergedString.append(word2[i])
            # attach the rest of the values from word2

        return ''.join(mergedString)