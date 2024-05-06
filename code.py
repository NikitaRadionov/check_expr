from itertools import product

ops = ('+', '-', '')

for op in product(ops, repeat=9):
    expression = '9{}8{}7{}6{}5{}4{}3{}2{}1{}0'.format(*op)
    if eval(expression) == 200:
        print(expression + '=200')
