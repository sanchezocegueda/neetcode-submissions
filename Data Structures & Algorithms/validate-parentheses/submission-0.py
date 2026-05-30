class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                match (c, top):
                    case (")", "(") | ("]", "[") | ("}", "{"):
                        pass
                    case _:
                        print(c, top)
                        return False
        
        return len(stack) == 0