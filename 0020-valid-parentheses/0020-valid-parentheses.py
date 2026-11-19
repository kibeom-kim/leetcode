class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        close_to_open = {
            ")": "(", 
            "]": "[", 
            "}": "{",
        }

        for c in s:
            if c in close_to_open.values():
                st.append(c)
            else:
                if len(st) == 0:
                    return False

                if st[-1] != close_to_open.get(c):
                    return False
                
                st.pop()
            
        if st:
            return False

        return True
