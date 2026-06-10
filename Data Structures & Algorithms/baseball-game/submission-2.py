class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = 0

        stack = []
        for op in operations:
            match op:
                case "+":
                    a, b = stack[-1], stack[-2]
                    stack.append(a + b)

                case "C":
                    stack.pop()

                case "D":
                    a = stack[-1]
                    stack.append(2 * a)
                
                case _:
                    stack.append(int(op))
        

        return sum(stack)
