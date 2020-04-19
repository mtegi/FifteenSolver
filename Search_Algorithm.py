from collections import deque
from copy import deepcopy
import numpy as np
from State import State


# wygeneruj poprawna ukladanke w zaleznosci od podanych wymiarow (np 4x4)
def generate_solution(width, height):
    ret = np.reshape(np.array([i for i in range(1, (width * height) + 1)]), (width, height))
    ret[width - 1][height - 1] = 0
    return ret


def is_not_back_move(state, direction):
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


def can_move(state, direction):
    if (state.zero_index[0] == 0 and direction == 'u') \
            or (state.zero_index[0] == state.height - 1 and direction == 'd') \
            or (state.zero_index[1] == 0 and direction == 'l') \
            or (state.zero_index[1] == state.width - 1 and direction == 'r'):
        return False
    return True


def generate_new_state(state, direction):
    values = deepcopy(state.values)
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
                 state.depth + 1, state.move_set.join(direction))


class SearchAlgorithm:
    def __init__(self, initial_state, search_order):
        self.state = initial_state
        self.solution = generate_solution(initial_state.width, initial_state.height)
        self.frontier = deque([initial_state])
        self.explored = set()
        self.max_depth = 0
        self.search_order = search_order
        self.move_set = ''
        self.visited = 1
        self.processed = 0

    def is_solution(self, state):
        return (state.values == self.solution).all()
