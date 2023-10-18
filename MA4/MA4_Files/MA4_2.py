#!/usr/bin/env python3.9

# Reviewer: 
# Student: Ifeoluwa Ojo

from cProfile import label
from person import Person
from numba import njit
from time import perf_counter_ns
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n - 1) + fib_py(n - 2)
	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n - 1) + fib_numba(n - 2)
	
def fib_cpp(n):
	f = Person(n)
	return f.fib()

if __name__ == '__main__':
	print(f'Fibonacci of 47 using C++ = {fib_cpp(47)}')
	print(f'Fibonacci of 47 using Numba = {fib_numba(47)}')
	nlst = []
	nlst2 = []
	t_py = []
	t_num = []
	t_num2 = []
	t_cpp = []
	t_cpp2 = []
	for n in range(20, 31):
		nlst.append(n)
		start = perf_counter_ns()
		fib_py(n)
		end = perf_counter_ns()
		t_py.append(end - start)
		start = perf_counter_ns()
		fib_numba(n)
		end = perf_counter_ns()
		t_num.append(end - start)
		start = perf_counter_ns()
		fib_cpp(n)
		end = perf_counter_ns()
		t_cpp.append(end - start)

	fig = plt.figure()
	ax = fig.add_subplot()
	ax.plot(nlst, t_py, "-b", label="Python")
	ax.plot(nlst, t_num, "-r", label="Numba")
	ax.plot(nlst, t_cpp, "-g", label='C++')
	ax.legend(loc="upper left")
	fig.savefig('Comparison_Py_Num_Ct.png')