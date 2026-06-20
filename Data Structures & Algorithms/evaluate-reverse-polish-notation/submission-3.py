import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),
        }

        for token in tokens:
            if re.match(r"-?\d", token) is not None:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                result = ops[token](operand1, operand2)
                stack.append(result)
        
        return stack.pop()