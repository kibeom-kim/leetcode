class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # paths = [[1] * n for _ in range(m)]

        # for i in range(1, m):
        #     for j in range(1, n):
        #         paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # return paths[m-1][n-1]

        previous = [1] * n

        for i in range(m - 1): 
            new_row = [1]
            idx = 1
            
            for j in range(n - 1): 
                new_row.append(new_row[idx - 1] + previous[idx])
                idx += 1

            previous = new_row

        return previous[-1]