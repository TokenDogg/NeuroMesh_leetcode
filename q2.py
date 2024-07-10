def brackets_checker(source):
    stack = []
    output = list((source + '.')[:-1])

    for i in range(len(source)):
        if source[i] == '(':
            output[i] = ' '
            stack.insert(0, i)
        elif source[i] == ')':
            if len(stack) == 0:
                output[i] = '?'
            else:
                output[i] = ' '
                stack.pop(0)

        else:
            output[i] = ' '
    for i in stack:
        output[i] = 'x'

    return ''.join(output)
print(brackets_checker('bge)))))))))'))
print(brackets_checker('((IIII))))))'))
print(brackets_checker('()()()()(uuu'))
print(brackets_checker('))))UUUU((()'))