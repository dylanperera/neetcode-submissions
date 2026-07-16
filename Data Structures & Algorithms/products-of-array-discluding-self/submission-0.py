class Solution:
    # Input: An array of numbers
    # Output: The array of numbers but the value at i

    # What if we had two arrays which represented prefix-products but they multiply in opposite directions
    # One prefix-product array starts from the left and calculates the prefix product
    # The other prefix-product array starts from the right and calculates the prefix product

    # We then loop through nums, get the left prefix-product array at index i-1 (if i != 0)
    # and also get the right prefix-product array at index i+1 (if i != len(nums)-1)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_length = len(nums)
        left_prefix_product = [_ for _ in nums]
        right_prefix_product = [_ for _ in nums]
        result = []

        for i in range(1, arr_length):
            left_prefix_product[i] *= left_prefix_product[i-1] 

        for i in range(arr_length - 2, -1, -1):
            right_prefix_product[i] *= right_prefix_product[i+1] 


        for i in range(0, arr_length):
            if i == 0:
                result.append(right_prefix_product[i+1])
            elif i == (arr_length - 1):
                result.append(left_prefix_product[i-1])
            else:
                result.append(left_prefix_product[i-1] * right_prefix_product[i+1])

        return result

            


