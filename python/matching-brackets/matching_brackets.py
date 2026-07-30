
"""Return True if all brackets in the input string are correctly matched."""
def is_paired(input_string):
    """

    Determine whether the brackets in the input string are balanced.



    Non-bracket characters are ignored.

    """
    stack = []
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for item in input_string:
        if item in pairs.values():
            stack.append(item)
        elif item in pairs:
            if not stack:
                return False
            if pairs[item] != stack[-1]:
                return False
            stack.pop()
        else:
            continue
    return not stack
