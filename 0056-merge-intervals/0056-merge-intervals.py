class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])

        answer = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            c = intervals[i]
            
            if prev[1] >= c[0]:
                prev = [prev[0], max(prev[1], c[1])]
            else:
                answer.append(prev)
                prev = c
        
        answer.append(prev)

        return answer