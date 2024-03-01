user_input = input().split()

operands = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
output = [''] * len(user_input)
stack = [''] * len(user_input)
output_index = 0
stack_index = 0

for symbol in user_input:
    if symbol.isnumeric():
        output[output_index] = symbol
        output_index += 1
    elif symbol == '(':
        stack[stack_index] = symbol
        stack_index += 1
    elif symbol == ')':
        while stack and stack[stack_index - 1] != '(':
            output[output_index] = stack[stack_index - 1]
            output_index += 1
            stack_index -= 1
        stack_index -= 1
    else:
        while (stack and stack_index > 0 and stack[stack_index - 1] in operands and
                operands[symbol] <= operands[stack[stack_index - 1]]):
            output[output_index] = stack[stack_index - 1]
            output_index += 1
            stack_index -= 1
        stack[stack_index] = symbol
        stack_index += 1

while stack_index > 0:
    output[output_index] = stack[stack_index - 1]
    output_index += 1
    stack_index -= 1

print(' '.join(output))
