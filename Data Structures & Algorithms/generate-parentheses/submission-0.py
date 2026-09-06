class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        parentheses = []

        def helper(i, j, curString, n):
            # print(i, j, curString, n, curString)
            if j == n:
                parentheses.append(curString)
                return
            
            if i < n:
                helper(i+1, j, curString + "(", n)
            
            if j < i:
                helper(i, j+1, curString + ")", n)
        
        helper(0, 0, "", n)

        return parentheses
                
            