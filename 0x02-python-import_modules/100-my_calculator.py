#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    """Comment."""
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)

    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if argv[2] in ops:
        n1, sym, n2 = map(int, [argv[1], argv[2], argv[3]])
        x = ops[sym](n1, n2)
        print('{:d} {} {:d} = {:d}'.format(n1, sym, n2, x))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    exit(0)
