class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        length = 0
        has_odd = False
        for count in d.values():
            if count % 2 == 0:
                length += count
            else:
                length += (count - 1)
                has_odd = True

        if has_odd:
            length += 1
            
        return length