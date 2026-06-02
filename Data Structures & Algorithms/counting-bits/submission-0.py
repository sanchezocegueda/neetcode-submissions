class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = []
        for i in range(n+1):
            # use hamming weight
            count = 0

            for j in range(10):
                if (1 << j & i) != 0:
                    count += 1

            ans.append(count)

        return ans