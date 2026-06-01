class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l_k = 1
        r_k = 0
        n = len(piles)
        for pile in piles:
            r_k = max(r_k, pile)
        
        # l_k is slowest rate, r_k is highest rate
        min_k = r_k
        while l_k < r_k:

            m_k = l_k + ((r_k - l_k) // 2) # middle value
            hours = 0
            # calculate time it would take to eat the bananas
            for pile in piles:
                hours += math.ceil (pile / m_k)

            # valid, try for better
            if hours <= h:
                min_k = min(min_k, m_k)
                r_k = m_k
            # too slow, need to up the k
            elif hours > h:
                l_k = m_k + 1
        
        return min_k
        