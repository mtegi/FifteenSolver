class State:

    def __init__(self, height, width, values, zero_index, depth, move_set):
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
