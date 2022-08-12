from jnumpy import init_jl, init_project
import time
start = time.time()
init_jl()
print("fft init_jl(): ", time.time()-start)
start = time.time()
init_project(__file__)
print("fft init_project(): ", time.time()-start, "\n")

from _fast_fft import jl_fft
