class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [1] * (n+1)
        
        if n == 1:
            return answer[n]

        answer[1] = 1
        answer[2] = 2

        

        for i in range(3, n+1):
            answer[i] = answer[i-1] + answer[i-2]

        return answer[n]
