input = [list('3SO2'), 1]

def recognition(input):
    for symbol in range(len(input[0])):
        try:
            if input[0][symbol].islower():
                input[0][symbol - 1] = input[0][symbol - 1] + input[0][symbol]
                input[0].remove(input[0][symbol])
            if symbol == 0:
                try:
                    input = [input[0][1:], int(input[0][0])]
                except:
                    None
            if input[0][symbol] == '(':
                dots = ''
                input[0][symbol] = (input[0][input[0].index(')') + 1]) + str(dots.join(input[0][symbol + 1: input[0].index(')')]))
                x = input[0][input[0].index(')') + 2:]
                input[0] = input[0][:symbol + 1]
                input[0].extend(x)
            if symbol != 0:
                try:
                    int(input[0][symbol])
                    input[0][symbol - 1] = input[0][symbol] + input[0][symbol - 1]
                    input[0].remove(input[0][symbol])
                except ValueError:
                    None
        except IndexError:
            None
    return input

print(recognition(input))

def definition(input):
    if len(input[0]) == 2 and 'O' in input[0][1]:
        input.append('oxide')
    print(input)

definition(recognition(input))