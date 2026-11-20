class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        amount = 0
        max_height = max(height)

        while left < right:
            amount = max(amount, (right-left)* min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            if max_height * (right - left) < amount:
                break
        
        return amount