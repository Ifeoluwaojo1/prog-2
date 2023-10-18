# Reviewer: William Samuelsson
# Student: Ifeoluwa Ojo
import random
import functools
import math

def points(d,n):
    return[[random.uniform(-1, 1) for x in range(d)] for i in range(n)]

def n_in_hyper(lst):
    pd = []
    for x in lst:
        xd = functools.reduce(lambda x, y: x + y, map(lambda x: x**2, x))
        if xd <= 1:
            pd.append(xd)
    return pd


def volume(d):
    vol_h = (math.pi ** (d/2)) / (math.gamma((d/2) + 1))
    return vol_h

def montecarlo(d, n):
    tot_points = points(d, n)
    nd = n_in_hyper(tot_points)
    approx_hyper = (len(nd) / len(tot_points)) * 2 ** d
    return approx_hyper

if __name__ == "__main__":
    d = 11
    n = 100000
    approx_hyper = montecarlo(d, n)
    vol_h = volume(d)
    print(f'The estimation of the volume of the d-dimensional hypersphere using Monte Carlo approximation is: {approx_hyper}')
    print(f'The real volume of the d-dimensional hypersphere is: {vol_h}')