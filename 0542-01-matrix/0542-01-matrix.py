class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        directions = [(0,1), (0, -1), (1,0), (-1,0)]

        q = deque()
        rows, cols = len(mat), len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = float('inf')
        
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                new_r, new_c = dr + r, dc + c

                if not(0 <= new_r < rows and 0 <= new_c < cols):
                    continue
                    
                if mat[new_r][new_c] > mat[r][c] + 1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    q.append((new_r, new_c))
        
        return mat