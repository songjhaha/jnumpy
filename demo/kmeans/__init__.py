from jnumpy import init_jl, init_project
import jnumpy as np
import time
init_jl()
start = time.time()
init_project(__file__)
print(time.time()-start)

from _fast_kmeans import _fast_kmeans


def jl_kmeans(x: np.ndarray, n_clusters: int):
    assignments, center = _fast_kmeans(x.T, n_clusters)
    return assignments, center.T
