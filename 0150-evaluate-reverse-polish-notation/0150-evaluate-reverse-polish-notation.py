class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = []

        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                st.append(int(token))
            else:
                right = st.pop()
                left = st.pop()

                if token == '+':
                    st.append(left + right)
                elif token == '-':
                    st.append(left - right)
                elif token == '*':
                    st.append(left * right)
                elif token == '/':
                    st.append(int(left / right))

        return st[-1]