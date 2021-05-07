import expression as ex

expr = input('Enter expression: ')
print('Result: ', ex.calc(ex.sort(ex.parse(''.join(expr.split())))))