from cython.parallel cimport prange
import numpy as np

def square_serial(double[:] inp):
    cdef int i,j,size
    cdef double[:] out
    size = inp.shape[0]
    out_np = np.empty(size, 'double')
    out = out_np
    
    for i in range(size):
        out[i] = inp[i]*inp[i]

    return out_np
    
def square_parallel(double[:] inp):
    cdef int i, size
    cdef double[:] out
    size = inp.shape[0]
    out_np = np.empty(size, 'double')
    out = out_np
    
    for i in prange(size, nogil=True):
        out[i] = inp[i]*inp[i]
    
    return out_np
