import parsing


input = '2Fe3(PO4)2'


def recognition(input):
    input = list(input)
    if input[0].isdigit():
        input = [input[1:], int(input[0])]
    else:
        input = [input, 1]

    for symbol in range(len(input[0])):
        if input[0][symbol].isdigit():
            input[0][symbol] = int(input[0][symbol])

    for symbol in range(len(input[0])):
        try:
            if input[0][symbol].islower():
                input[0][symbol-1] = input[0][symbol-1] + input[0][symbol]
                input[0].remove(input[0][symbol])
        except:
            pass

    for symbol in range(len(input[0])):
        if input[0][symbol] in parsing.all_elements:
            if type(input[0][symbol + 1]) == int:
                quantity = input[0][symbol + 1]
            else:
                quantity = 1
            input[0][symbol] = element(input[0][symbol], quantity)

    global acid_residue_quantity
    if ')' in input[0]:
        try:
            acid_residue_quantity = input[0][input[0].index(')')+1]
        except:
            acid_residue_quantity = 1

    for symbol in range(len(input[0])):
        try:
            if type(input[0][symbol]) == int:
                input[0].remove(input[0][symbol])
        except:
            pass

    if len(input[0]) > 2:

        if '(' in input[0]:
            for symbol in range(len(input[0])):
                if input[0][symbol] == '(':
                    input[0][symbol] = input[0][input[0].index(input[0][symbol+1]) : input[0].index(')')]
                    input[0][input[0].index(input[0][symbol + 1]): input[0].index(')')+1] = []
                    input[0][1].append(acid_residue_quantity)
                    break
        else:
            input[0] = [input[0][1], input[0][1:]]

        input[0][1] = acid_residue(input[0][1][0], input[0][1][1], input[0][1][2])

    return input


class element(object):

    def __init__(self, element_name, quantity):
        if element_name not in parsing.all_elements:
            raise KeyError
        self.element_name = element_name
        self.quantity = quantity
        self.possible_valence = parsing.valence[element_name]
        if len(parsing.valence[element_name]) == 1:
            self.valence = parsing.valence[element_name][0]


class acid_residue(object):

    def __init__(self, first_element, second_element, quantity):
        self.first_element = first_element
        self.second_element = second_element
        self.quantity = quantity


class matter(object):

    def __init__(self, first_element, rest):
        self.first_element = first_element
        if type(rest) == acid_residue:
            self.acid_residue = rest
        else:
            self.second_element = rest


print(recognition(input))