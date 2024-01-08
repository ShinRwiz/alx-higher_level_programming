#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t_total = ()
    a1 = tuple_a + (0, 0)
    b2 = tuple_b + (0, 0)
    t_total = a1[0] + b2[0], a1[1] + b2[1]
    return t_total
