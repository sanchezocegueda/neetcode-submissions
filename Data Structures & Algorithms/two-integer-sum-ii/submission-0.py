class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        l = 0
        r = n-1

        while True:

            two_sum = numbers[l] + numbers[r]
            
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            else:
                break

        return [l + 1, r + 1]
