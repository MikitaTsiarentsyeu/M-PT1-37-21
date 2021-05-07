math_oper = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y), '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}
 
def parse(expr):
    new_str = ''
    for i in expr:
        if not new_str and i in '-':
            new_str += i
            continue
        if i in '1234567890':
            new_str += i
        elif new_str:
            yield float(new_str)
            new_str = ''
        if i in math_oper or i in '()':
            yield i
    if new_str:
        yield float(new_str)
 
def sort(parsed):
    l = []
    for i in parsed:
        if i in math_oper:
            while l and l[-1] != '(' and math_oper[i][0] <= math_oper[l[-1]][0]:
                yield l.pop()
            l.append(i)
        elif i == ')':
            while l:
                x = l.pop()
                if x == '(':
                    break
                yield x
        elif i == '(':
            l.append(i)
        else:
            yield i
    while l:
        yield l.pop()
 
def calc(sort):
    l = []
    for i in sort:
        if i in math_oper:
            y = l.pop()
            x = l.pop()
            l.append(math_oper[i][1](x, y))
        else:
            l.append(i)
    return sum(l)