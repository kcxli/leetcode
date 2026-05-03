class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        value = 0

        if (len(tokens) < 3):
            return int(tokens[0])


        for token in tokens:
            if (token not in operators):
                stack.append(token)
            elif (token == '+'):
                x = int(stack.pop())
                y = int(stack.pop())
                value = x + y 
                stack.append(value)
            elif (token == '*'):
                x = int(stack.pop())
                y = int(stack.pop())
                value = x * y 
                stack.append(value)
            elif (token == '/'):
                x = int(stack.pop())
                y = int(stack.pop())
                value = (y//1) / (x//1)
                stack.append(value)
            elif (token == '-'):
                x = int(stack.pop())
                y = int(stack.pop())
                value = y - x
                stack.append(value)

        return math.trunc(value)

        