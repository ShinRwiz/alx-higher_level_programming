#!/usr/bin/python3
for i in range(ord('A'), ord('z') + 1):
    if i % 2 == 0:
        print('{:c}'.format(122 - i), end='')
    else:
        print('{:c}'.format(90 - i), end='')
