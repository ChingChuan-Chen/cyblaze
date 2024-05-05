# cython: language_level = 3
# cython: language = c++
# cython: boundscheck = False
# cython: wraparound = False
# cython: cdivision = True
import numpy as np
cimport numpy as np

cdef np.ndarray[double, ndim=2] ndarray_double():
    return np.empty(dtype='double')
