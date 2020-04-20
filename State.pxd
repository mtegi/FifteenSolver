cimport numpy as np

cdef class State:
    cdef readonly height
    cdef readonly int width
    cdef readonly np.ndarray values
    cdef readonly (int,int) zero_index
    cdef readonly int depth
    cdef readonly str move_set
