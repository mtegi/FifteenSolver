from collections import deque


# wygeneruj poprawna ukladanke w zaleznosci od podanych wymiarow (np 4x4)
def generate_solution(state):
    ret = []
    j = 1
    for i in range(state.width):
        ret.append([j for j in range(j, j + state.height)])
        j = j + state.height
    ret[state.width - 1][state.height - 1] = 0
    return ret


class SearchAlgorithm:
    def __init__(self, initial_state, search_order):
        self.state = initial_state
        self.solution = generate_solution(initial_state)
        self.frontier = deque([initial_state])
        self.explored = deque()
        self.max_depth = 0
        self.search_order = search_order
        self.move_set = ''
        self.visited = 1
        self.processed = 0

    def is_solution(self, state):
        return state.values == self.solution

    def is_not_back_move(self, direction):
        try:
            last_move = self.move_set[-1]
        except IndexError:
            return True
        if (last_move == 'd' and direction == 'u') \
                or (last_move == 'u' and direction == 'd') \
                or (last_move == 'r' and direction == 'l') \
                or (last_move == 'l' and direction == 'r'):
            return False
        return True
