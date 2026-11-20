class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]

        if start_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        visited = [[False] * cols for _ in range(rows)]

        adj_dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        st = []
        st.append((sr, sc))
        while st:
            r, c = st.pop()

            image[r][c] = color 
            visited[r][c] = True

            for adj_dir in adj_dirs:
                adj_r, adj_c = r + adj_dir[0], c + adj_dir[1]
                
                if not(0 <= adj_r < len(image) and 0 <= adj_c < len(image[0])):
                    continue

                if not visited[adj_r][adj_c] and start_color == image[adj_r][adj_c]:
                    st.append((adj_r, adj_c))
        
        return image