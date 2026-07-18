class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)

        l, r = 0, 0
        running_sum = 0
        count = 0
        while r < k:
            running_sum += arr[r]
            r += 1
        
        if (running_sum / k) >= threshold:
            count += 1

        while r < n:
            running_sum -= arr[l]
            l += 1
            running_sum += arr[r]
            r += 1

            if (running_sum / k) >= threshold:
                count += 1

        
        return count