class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack: List[int] = []
        for token in tokens:
            print(stack)
            match token:
                case "+":
                    r, l = stack.pop(), stack.pop()
                    stack.append(l + r)
                case "-":
                    r, l = stack.pop(), stack.pop()
                    stack.append(l - r)
                case "*":
                    r, l = stack.pop(), stack.pop()
                    stack.append(l * r)
                case "/":
                    r, l = stack.pop(), stack.pop()
                    stack.append(int(l / r))
                case _:
                    stack.append(int(token))
        
        return stack.pop()