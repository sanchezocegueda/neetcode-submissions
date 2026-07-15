class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = []
        m = len(image)
        n = len(image[0])

        marked = set()

        stack.append((sr, sc))

        while stack:

            i, j = stack.pop()

            if (i, j) in marked:
                continue

            marked.add((i, j))

            # up
            if i > 0 and image[i-1][j] == image[i][j]:
                stack.append((i-1, j))

            # down
            if i < m - 1 and image[i+1][j] == image[i][j]:
                stack.append((i+1, j))

            # left
            if j > 0 and image[i][j-1] == image[i][j]:
                stack.append((i, j-1))

            # right
            if j < n-1 and image[i][j+1] == image[i][j]:
                stack.append((i, j+1))
            
            image[i][j] = color

        return image