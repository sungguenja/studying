import mine_stack

def check_bracket_function(statement):
    stack = mine_stack.Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            check = stack.pop()
            if check == "isEmpty":
                return False
            else:
                if (ch == '{' and check != '}') or (ch == '[' and check != ']') or (ch == '(' and check != ')'):
                    return False
    
    return stack.isEmpty()