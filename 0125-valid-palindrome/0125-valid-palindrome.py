class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ""
        for c in s:
            if c.isalnum():
                filtered_s += c.lower()
            
        l = len(filtered_s)
        for i in range(0, l // 2):
            if filtered_s[i] != filtered_s[l - i - 1]:
                return False

        return True