from jnumpy import init_jl, init_project
import jnumpy as np
import time
start = time.time()
init_jl()
print("init_jl(): ", time.time()-start)
start = time.time()
init_project(__file__)
print("kmeans init_project(): ", time.time()-start, "\n")

from _fast_kmeans import _fast_kmeans


def jl_kmeans(x: np.ndarray, n_clusters: int):
    assignments, center = _fast_kmeans(x.T, n_clusters)
    return assignments, center.T
