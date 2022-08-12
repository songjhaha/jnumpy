from jnumpy import init_jl, init_project
import time
start = time.time()
init_jl()
print("basic init_jl(): ", time.time()-start)
start = time.time()
init_project(__file__)
print("basic init_project(): ", time.time()-start, "\n")

from _basic import jl_int_add, jl_mat_mul
