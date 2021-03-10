import mine_stack

def evak_postfix(expr):
    stack = mine_stack.Stack()
    for token in expr:
        if token in "+-*/":
            val2 = stack.pop()
            val1 = stack.pop()
            if token == "+":
                stack.push(val1+val2)
            elif token == "-":
                stack.push(val1-val2)
            elif token == "*":
                stack.push(val1*val2)
            elif token == "/":
                stack.push(val1/val2)
        else:
            stack.push(float(token))
    return stack.pop()