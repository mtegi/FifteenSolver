cimport numpy as np

cdef class State:
    cdef readonly int width, height, depth
    cdef readonly str move_set
    cdef readonly np.ndarray values
    cdef readonly (int, int) zero_index

    def __init__(self, int height, int width,np.ndarray values, (int, int)zero_index, int depth, str move_set):
        self.height = height
        self.width = width
        self.values = values
        self.zero_index = zero_index
        self.depth = depth
        self.move_set = move_set

    def __eq__(self, other):
        if hash(self.values.tobytes()) == hash(other.values.tobytes()):
            return True
        return False

    def __ne__(self, other):
        if hash(self.values.tobytes()) != hash(other.values.tobytes()):
            return True
        return False

    def __hash__(self):
        return hash(self.values.tobytes())
