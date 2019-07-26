import parsing


input = '2Fe3(PO4)2'


def recognition(input):
    input = list(input)
    if input[0].isdigit():
        input = [input[1:], int(input[0])]
    else:
        input = [input, 1]
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
            print(input[0])
            print(input[0][symbol])
            if input[0][symbol] == '(':
                print(input[0])
                input[0][symbol] = input[0][input[0].index('(') : input[0].index(')')]
#                dots = ''
#                input[0][symbol] = (input[0][input[0].index(')') + 1]) + str(dots.join(input[0][symbol + 1: input[0].index(')')]))
#                x = input[0][input[0].index(')') + 2:]
#                input[0] = input[0][:symbol + 1]
#                input[0].extend(x)
                print(input, 1)
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
            for x in parsing.valence.keys():
                if symbol[0] == x and len(parsing.valence[x]) == 1:
                        input[0][input[0].index(symbol)].append(parsing.valence[symbol[0]][0])

    if len(input[0]) == 2 and input[0][1][0] == 'O':
        input.append(['oxide'])
    else:
        input[0] = [input[0][0], input[0][1:]]
        input[0][1] = [input[0][1]]
#        print(input)
        input[0][1] = [input[0][1][0], acid_residue_valence(input)]

    if input[0][0][2] == 'metal':
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
        acid_residue(input)
        input.append('acid')


    determinded_valence = 0
    for x in input[0][1][0]:
        if len(x) == 4:
            determinded_valence += int(x[1]) * x[3]

    for y in input[0][1][0]:
        if len(y) == 3:
            input[0][1][0][input[0][1][0].index(y)].append(determinded_valence // int(y[1]) - int(input[0][1][1]))
            if input[0][1][0][input[0][1][0].index(y)][3] not in parsing.valence[input[0][1][0][input[0][1][0].index(y)][0]]:
                raise KeyError

    print(input[0][0])
#    if len(input[0][0]) == 3:
#        input[0][0].append(int(input[0][1][3])*)

#        print(input)
#    if input[0][0][1]*input[0][0][3] != input[0][1][1]*input[0][1][3]:
#        raise TypeError
    print(input)


def acid_residue_valence(input):
    for b in parsing.table:
        for c in b:
#            print(c[0], acid_residue(input))
            if c[0] == acid_residue(input):
                return c[1][0]
    raise ValueError

def acid_residue(input):
    result = ''
    for a in input[0][1][0]:
        if input[0][1][0].index(a) != 0:
            result += a[0].lower()
#            print(result)
        else:
            result += a[0][0]
#            print(result)
        if a[1] != '1':
            result += a[1][0]
#            print(result)
    return result

print(recognition(input))
#definition(recognition(input))