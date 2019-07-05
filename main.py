import parsing


input = [list('2H2So4'), 1]


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
                    input[0][symbol - 1] = [input[0][symbol - 1], input[0][symbol]]
                    input[0].remove(input[0][symbol])
                except ValueError:
                    None
        except IndexError:
            None
    for symbol in input[0]:
        if type(symbol) == str:
            input[0][input[0].index(symbol)] = [symbol, '1']
    return input

def definition(input):
    for symbol in input[0]:
        if symbol[0] in parsing.all_elements:
            if symbol[0] in parsing.non_metals:
                input[0][input[0].index(symbol)].append('non_metal')
            else:
                input[0][input[0].index(symbol)].append('metal')
    if len(input[0]) == 2 and input[0][1][0] == 'O':
        input.append(['oxide'])
    elif input[0][0][2] == 'metal':
        result = ''
        for x in input[0][1:]:
            result += x[0]
            if x[1] != '1':
                result += x[1]
        if result[:2] == 'OH':
            input.append('ground')
        else:
            for y in parsing.table:
                for z in y:
                    if z[0] == result:
                        input.append('salt')
    elif input[0][0][0] == 'H':
        result = ''
        for a in input[0][1:]:
            result += a[0]
            if a[1] != '1':
                result += a[1]
                print(result)
        for b in parsing.table:
            for c in b:
                if c[0] == result:
                    input.append('acid')
    print(input)


definition(recognition(input))