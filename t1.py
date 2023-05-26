def check_brackets(text):
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']
    stack = []

    for i, char in enumerate(text):
        if char in opening_brackets:
            stack.append((char, i))
        elif char in closing_brackets:
            if len(stack) == 0:
                return i
            top = stack.pop()
            if top[0] != opening_brackets[closing_brackets.index(char)]:
                return i+1

    if len(stack) == 0:
        return "Success"
    else:
        return stack[0][1]

#Примеры
print(check_brackets("[]"))
print(check_brackets("{}[]"))
print(check_brackets("[()]"))
print(check_brackets("{[]}()"))
print(check_brackets("{[}"))
print(check_brackets("foo(bar);"))
print(check_brackets("foo(bar[i);"))