from collections import deque
from copy import deepcopy
import numpy as np
cimport numpy as np
from libcpp cimport bool
from State cimport State
DTYPE = np.int
ctypedef np.int_t DTYPE_t

# wygeneruj poprawna ukladanke w zaleznosci od podanych wymiarow (np 4x4)
cdef np.ndarray generate_solution(int width, int height):
    ret = np.reshape(np.array([i for i in range(1, (width * height) + 1)], dtype=DTYPE), (width, height))
    ret[width - 1][height - 1] = 0
    return ret


cpdef is_not_back_move(state: State, direction:str):
    try:
        last_move = state.move_set[-1]
    except IndexError:
        return True
    if (last_move == 'd' and direction == 'u') \
            or (last_move == 'u' and direction == 'd') \
            or (last_move == 'r' and direction == 'l') \
            or (last_move == 'l' and direction == 'r'):
        return False
    return True


cpdef can_move(State state, str direction):
    if (state.zero_index[0] == 0 and direction == 'u') \
            or (state.zero_index[0] == state.height - 1 and direction == 'd') \
            or (state.zero_index[1] == 0 and direction == 'l') \
            or (state.zero_index[1] == state.width - 1 and direction == 'r'):
        return False
    return True


cpdef State generate_new_state(State state, str direction):
    values = deepcopy(state.values)
    depth = state.depth
    zero_index = [state.zero_index[0], state.zero_index[1]]
    if direction == 'l':
        values[zero_index[0]][zero_index[1]], values[zero_index[0]][zero_index[1] - 1] \
            = values[zero_index[0]][zero_index[1] - 1], values[zero_index[0]][zero_index[1]]
        zero_index[1] -= 1
    elif direction == 'r':
        values[zero_index[0]][zero_index[1]], values[zero_index[0]][zero_index[1] + 1] \
            = values[zero_index[0]][zero_index[1] + 1], values[zero_index[0]][zero_index[1]]
        zero_index[1] += 1
    elif direction == 'u':
        values[zero_index[0]][zero_index[1]], values[zero_index[0] - 1][zero_index[1]] \
            = values[zero_index[0] - 1][zero_index[1]], values[zero_index[0]][zero_index[1]]
        zero_index[0] -= 1
    elif direction == 'd':
        values[zero_index[0]][zero_index[1]], values[zero_index[0] + 1][zero_index[1]] \
            = values[zero_index[0] + 1][zero_index[1]], values[zero_index[0]][zero_index[1]]
        zero_index[0] += 1
    return State(state.height, state.width, values, (zero_index[0], zero_index[1]),
                 depth + 1, "".join([state.move_set, direction]))


class SearchAlgorithm:
    def __init__(self, initial_state: State, search_order: str):
        self.state = initial_state
        self.solution = generate_solution(initial_state.width, initial_state.height)
        self.frontier = deque([initial_state])
        self.explored = set()
        self.max_depth = 0
        self.search_order = search_order
        self.move_set = ''
        self.visited = 1
        self.processed = 0

    def is_solution(self, state: State) -> bool:
        return (state.values == self.solution).all()
