#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    elif len(tuple_a) > 2:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) > 2:
        tuple_b = tuple_b[:2]
    v = ()
    for i in range(2):
        v += (tuple_a[i] + tuple_b[i],)
    return v
