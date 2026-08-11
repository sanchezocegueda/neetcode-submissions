class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [1]

        for i in range(1, rowIndex+1):
            lenRow = i+1
            newRow = [0] * lenRow

            for j in range(lenRow):
                if j-1 >= 0:
                    newRow[j] += pascal[j-1]
                
                if j < i:
                    newRow[j] += pascal[j]
            
            pascal = newRow
        
        return pascal

    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]

        for i in range(1, numRows):
            lenRow = i+1
            newRow = [0] * lenRow

            for j in range(lenRow):
                if j-1 >= 0:
                    newRow[j] += pascal[i-1][j-1]
                
                if j < i:
                    newRow[j] += pascal[i-1][j]
            
            pascal.append(newRow)


        return pascal