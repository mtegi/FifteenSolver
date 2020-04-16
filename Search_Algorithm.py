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
        # aktualny stan
        self.state = initial_state
        # rozwiazanie
        self.solution = generate_solution(initial_state)
        # stany do sprawdzenia
        self.frontier = deque([initial_state])
        # stany sprawdzone
        self.explored = deque()
        # maks glebokosc rekursji
        self.max_depth = 0
        # kolejnosc przeszukiwania
        self.search_order = search_order
        # kolejnosc ruchow
        self.move_set = ''
        # stany odwiedzone
        self.visited = 1
        # stany przetworzone
        self.processed = 0

    # czy znaleziono rozwiazanie?
    def found_solution(self):
        if self.state.values == self.solution:
            return True
        else:
            return False

    def is_solution(self, state):
        if state.values == self.solution:
            return True
        else:
            return False

    def update_counters(self):
        self.processed = len(self.explored)

    # czy sie nie cofamy?
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

    # wygeneruj sasiednie stany
    def generate_next_states(self):
        new_states = []
        for direction in self.search_order:
            if self.state.can_move(direction) and self.is_not_back_move(direction):
                new_states.append(self.state.generate_new_state(direction))
        return new_states
