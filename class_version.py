import parsing


input = '2FeSO4'
matter_name = input


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

        if len(input[0][1]) == 2:
            quantity = 1
        else:
            quantity = input[0][1][2]

        print(input[0][0])
        input[0][1] = acid_residue(input[0][1][0], input[0][1][1], quantity)

    elif input[0][1].name != 'O':
        input[0][1] = acid_residue(input[0][1], quantity=input[1])

    return matter(input[0][0], input[0][1], input[1])


class element(object):

    def __init__(self, name, quantity=1):
        if name not in parsing.all_elements:
            raise KeyError

        self.name = name
        self.quantity = quantity
        self.possible_valence = parsing.valence[name]
        if len(parsing.valence[name]) == 1:
            self.valence = parsing.valence[name][0]
        else:
            self.valence = None

        if self.name in parsing.non_metals:
            self.type = 'non_metal'
        else:
            self.type = 'metal'

    def __str__(self):
        return self.name


class acid_residue(object):

    def __init__(self, first_element, second_element=None, quantity=1):
        self.first_element = first_element
        self.second_element = second_element
        self.quantity = quantity

        self.name = ''
        for x in [self.first_element, self.second_element]:
            if x is None:
                break
            self.name += x.name
            if x.quantity > 1 and self.second_element is not None:
                self.name += str(x.quantity)

        for x in parsing.table:
            for y in x:
                if y[0].upper() == self.name.upper():
                    if len(y[1]) == 2:
                        self.valense = int(y[1][0])
                    else:
                        self.valense = 1
                    break

        if self.second_element is None:
            self.first_element.valence = self.valense

        else:
            for x in [self.first_element, self.second_element]:
                if x.valence is None:
                    for y in [self.first_element, self.second_element]:
                        if y != x:
                            x.valence = (y.valence*y.quantity - self.valense) / x.quantity

        if type(self.valense) != int:
            raise ValueError

        if self.quantity > 1 and second_element is not None:
            self.name = '(' + self.name + ')'

    def __str__(self):
        return self.name


class matter(object):

    def __init__(self, first_element, rest, quantity=1):
        self.quantity = quantity
        self.first_element = first_element
        self.rest = rest

        self.name = ''
        if self.quantity > 1:
            self.name += str(quantity)
        for x in [self.first_element, self.rest]:
            self.name += x.name
            if x.quantity > 1:
                self.name += str(x.quantity)

    def __str__(self):
        return self.name


print(recognition(input))