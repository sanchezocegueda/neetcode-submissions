class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        lm, rm = 0, m
        ln, rn = 0, n

        while lm < rm:
            i = lm + ((rm - lm) // 2)
            
            # smaller and larger numbers
            smaller = matrix[i][0]
            larger = matrix[i][n-1]
            if target < smaller:
                rm = i
            elif target > larger:
                lm = i + 1
            else:
                # smaller <= target <= larger
                while ln < rn:
                    j = ln + ((rn - ln) // 2)
                    mij = matrix[i][j]

                    if mij > target:
                        rn = j
                    elif mij < target:
                        ln = j + 1
                    else: 
                        return True
                return False
            
        return False