class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        idxa, idxb = len(a) - 1, len(b) - 1

        while idxa >= 0 or idxb >= 0 or carry == 1:
            if idxa >= 0:
                carry += int(a[idxa])
                idxa -= 1
            
            if idxb >= 0:
                carry += int(b[idxb])
                idxb -= 1
            
            result.append(str(carry % 2))
            carry = carry // 2
        
        return "".join(result[::-1])

        # int_a = int(a, 2)
        # int_b = int(b, 2)
        
        # res = int_a + int_b

        # return (bin(res)[2:])