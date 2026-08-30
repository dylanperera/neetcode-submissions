class Solution:

    # We have these operations which are given by the input list
    # 1. '+' -> get previous last elements of the stack and sum, then add to stack
    # 2. 'D' -> get the last element in the stack and double it, then add to stack
    # 3. 'C' -> remove the previous score
    # 4. integer -> add to score

    # Stack because the inputs are interacting with one another -> should only contain integers

    def calPoints(self, operations: List[str]) -> int:
        stack = []
        stack_sum = 0
        # loop through the operations
        for op in operations:
            # check if +
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            # elif D
            elif op == 'D':
                stack.append(stack[-1] * 2)
            # elif C
            elif op == 'C':
                stack.pop()
            # else convert to integer and add to stack
            else:
                stack.append(int(op))


        for score in stack:
            stack_sum += score

        return stack_sum