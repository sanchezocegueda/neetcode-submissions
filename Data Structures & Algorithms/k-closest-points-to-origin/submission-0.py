class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        dist_sq = lambda x: x[0] ** 2 + x[1] ** 2
    
        def partition(l, r):
            pivotIdx = r
            
            i = l
            pivotDist = dist_sq(points[pivotIdx])
            for j in range(l, r):
                if dist_sq(points[j]) <= pivotDist: # smaller element, swap w bigger on left
                    points[i], points[j] = points[j], points[i]
                    i += 1
                
            points[i], points[pivotIdx] = points[pivotIdx], points[i]
            return i # new location of pivot
        
        L, R = 0, len(points)-1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k: # search in right half
                L = pivot + 1
            else:
                R = pivot - 1
        
        return points[:k]