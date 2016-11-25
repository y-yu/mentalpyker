from charm.toolbox.ecgroup import ECGroup, G, ZR
from charm.toolbox.eccurve import prime192v1, prime192v2
from charm.core.math.integer import integer, toInt

import random
from functools import reduce

group = ECGroup(prime192v1)
#group.paramgen(256)

# Utility Functions

def random_point():
    return group.random(G)

def random_number():
    return group.random()

def make_pi(n):
    xs = range(n)
    random.shuffle(xs)
    return xs

def make_sigma(m, n):
    return make_pi(n - m)

def permute(pi, d):
    assert len(pi) == len(d)
    return [d[i] for i in pi]

def compose(pi2, pi1):
    assert len(pi1) == len(pi2)
    return [pi1[i] for i in pi2]

def inverse(pi):
    xs = [(pi[i], i) for i in range(len(pi))]
    return [x[1] for x in sorted(xs)]

def mask(s):
    return [random.choice([True, False]) for _ in range(s)]

# operation

def make_points(n):
    return [random_point() for _ in range(n)]
