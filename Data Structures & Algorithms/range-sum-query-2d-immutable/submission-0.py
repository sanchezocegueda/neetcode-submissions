class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.diagSum = [[0 for _ in range(n)] for _ in range(m)]



        
        for i in range(m):
            for j in range(n):
                up = self.diagSum[i-1][j] if i > 0 else 0
                left = self.diagSum[i][j-1] if j > 0 else 0
                diagonal = self.diagSum[i-1][j-1] if (i > 0 and j > 0) else 0
                self.diagSum[i][j] = matrix[i][j] + up + left - diagonal

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        big_square = self.diagSum[row2][col2]

        left_square = self.diagSum[row2][col1-1] if col1 > 0 else 0
        up_square = self.diagSum[row1-1][col2] if row1 > 0 else 0
        diag_square = self.diagSum[row1-1][col1-1] if (row1 > 0 and col1 > 0) else 0

        return big_square - left_square - up_square + diag_square
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)