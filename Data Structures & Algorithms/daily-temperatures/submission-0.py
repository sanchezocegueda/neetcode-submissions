class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                time = i - idx
                result[idx] = time

            stack.append(i)
        
        return result
            