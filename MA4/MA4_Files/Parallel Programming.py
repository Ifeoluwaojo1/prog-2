# Reviewer: 
# Student: Ifeoluwa Ojo

import random
import functools
import math
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future

def points(d, n):
    return[[random.uniform(-1, 1) for x in range(d)] for i in range(n)]

def n_in_hyper(lst):
    pd = []
    for x in lst:
        xd = functools.reduce(lambda x, y: x + y, map(lambda x: x ** 2, x))
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
    n_processes = 10
    start = pc()
    approx_hyper = montecarlo(d, n)
    end = pc()
    print(f'The estimation of the volume of the d-dimensional hypersphere using Monte Carlo approximation is: {approx_hyper}')
    print(f'The estimation of the volume of the d-dimensional hypersphere using Monte Carlo approximation took: {round(end - start, 2)} second')

    start = pc()
    approx_hyper = 0.
    with future.ProcessPoolExecutor() as ex:
        processes = []
        for _ in range(n_processes):
            p = ex.submit(montecarlo, d, int(n / n_processes))
            processes.append(p)
        for i in range(len(processes)):
            approx_hyper += processes[i].result()
        approx_hyper /= n_processes #try integer division res=ex.map(montecarlo, [d]*10, [n//n_processes]*10)

    end = pc()
    print(f'The estimation of the d-dimensional hypersphere using Monte Carlo approximation is: {approx_hyper}')
    print(f'The estimation of the d-dimensional hypersphere using Monte Carlo approximation took {round(end - start, 2)} second')