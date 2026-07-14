class NumMatrix:

    # Since sumRegion must run O(1) that means we must utilize a pre-fix sum to quickly calculate the sums of different matricies
    
    # Need to create a pre-fix sum matrix per row
    # The prefix-sum of a point (i,j) is the row up to j plus (i-1, j)
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.prefix_sum_mat = [[0] * COLS for r in range(0,ROWS)]

        for row in range(0, ROWS):
            prefix_sum_row = 0
            for col in range(0, COLS):
                prefix_sum_row = matrix[row][col] + prefix_sum_row
                self.prefix_sum_mat[row][col] = prefix_sum_row

                if row != 0:
                    self.prefix_sum_mat[row][col] += self.prefix_sum_mat[row-1][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum_mat[row2][col2]
        if row1 != 0:
            total -= self.prefix_sum_mat[row1-1][col2]
        
        if col1 != 0:
            total -= self.prefix_sum_mat[row2][col1-1]

        if row1 != 0 and col1 != 0:
            total += self.prefix_sum_mat[row1-1][col1-1]

        return total


# Your NumMatrix object will be instantiated and called as such:

# param_1 = obj.sumRegion(row1,col1,row2,col2)