class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['*', '+', '/', '-']
        for tok in tokens:
            if tok in operators:
                n1 = stack.pop()
                n2 = stack.pop()

                if tok == '*':
                    stack.append(n1 * n2)
                elif tok == '+':
                    stack.append(n1 + n2)
                elif tok == '-':
                    stack.append(n2 - n1)
                else:
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(tok))

        return stack.pop()