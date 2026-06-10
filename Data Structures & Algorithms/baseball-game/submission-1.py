class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = 0

        stack = []
        for op in operations:
            match op:
                case "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b)
                    stack.append(a)
                    stack.append(a + b)

                case "C":
                    stack.pop()

                case "D":
                    a = stack.pop()
                    stack.append(a)
                    stack.append(2 * a)
                
                case _:
                    stack.append(int(op))
        

        return sum(stack)
