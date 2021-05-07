from decimal import Decimal

def change(money, cost):
    ex_change = Decimal(money) - Decimal(cost)
    new_str = ''
    for i in coin:
        if ex_change // Decimal(i):
            new_str += f'{i}: {ex_change // Decimal(i)}\n'
            ex_change = ex_change - (ex_change // Decimal(i)) * Decimal(i)
    return new_str


coin = ('2', '1', '0.5', '0.2', '0.1', '0.05', '0.02', '0.01')
print(change('15.00', '4.15'))