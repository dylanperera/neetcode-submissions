class Solution:
    # Input: String consisting of the characters '(', ')', '{', '}', '[', ']'
    # Output: Determine if the string s satifies all conditions

    # Elements interact with each other
    def isValid(self, s: str) -> bool:
        # If we encounter a closing bracket, the most recent bracket we have seen prior to that must be the same but opening
        # If we're looking for the most recent opening bracket, then a stack of LIFO is the best option
        stack = []

        for ch in s:
            if ch == '}' or ch == ')' or ch == ']':
                if len(stack) == 0:
                    return False
                
                mostRecent = stack.pop()

                if ch == '}' and mostRecent != '{':
                    return False

                if ch == ']' and mostRecent != '[':
                    return False

                if ch == ')' and mostRecent != '(':
                    return False

            else:
                stack.append(ch)

                
        return len(stack) == 0