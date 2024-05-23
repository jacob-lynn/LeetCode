
def is_valid_parentheses(s: str) -> bool:
    stack = []
    parens = {"(":")",
                "{":"}",
                "[":"]"}
    for chr in s:
        if chr in parens:
            stack.append(parens[chr])
        else:
            if not stack or chr != stack.pop():
                return False
    return not stack

                
                


