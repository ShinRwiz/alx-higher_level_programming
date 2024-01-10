#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    if not s or isinstance(s, str):
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    t = 0
    for i in range(len(s)):
        if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
            t -= d[s[i]]
        else:
            t += d[s[i]]
    return t
