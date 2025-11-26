class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # stack holds scores at each depth; start with base 0
        for char in s:
            if char == '(':
                stack.append(0)
            else:  # char == ')'
                val = stack.pop()  # score inside the current deepest "( ... )"
                # if nothing inside → "()", score = 1; else 2 * val
                score = 1 if val == 0 else 2 * val
                stack[-1] += score  # add to the enclosing level
        return stack[0]
