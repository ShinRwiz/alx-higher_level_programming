#!/usr/bin/python3
for i in range(ord('A'), ord('z') + 1):
    if i % 2 == 0:
        print('{:c}'.format(ord('z') - (i - ord('A'))), end='')
    else:
        print('{:c}'.format(i), end='')
