from copy import deepcopy

def index_2d(data, search):
    for i, e in enumerate(data):
        try:
            return [i, e.index(search)]
        except ValueError:
            continue


class State:
    def __init__(self, data):
        self.height = data[0]
        self.width = data[1]
        self.values = []
        j = 2
        # wczytaj klocki ukladanki
        for i in range(self.width):
            self.values.append(data[j:j + self.height])
            j = j + self.height
        # znajdz gdzie jest zero
        self.zero_index = index_2d(self.values, 0)
        self.depth = 1
        self.move_set = ""

# override ==
    def __eq__(self, other):
        if self.values == other.values:
            return True
        return False

# override !=
    def __ne__(self, other):
        if self.values != other.values:
            return True
        return False

# mozna wykonac ruch w danym kierunku
    def can_move(self, direction):
        if (self.zero_index[0] == 0 and direction == 'u') \
                or (self.zero_index[0] == self.height - 1 and direction == 'd') \
                or (self.zero_index[1] == 0 and direction == 'l') \
                or (self.zero_index[1] == self.width - 1 and direction == 'r'):
            return False
        return True

    def generate_new_state(self, direction):
        # sklonuj siebie
        ret = deepcopy(self)
        if direction == 'l':
            #swap
            ret.values[ret.zero_index[0]][ret.zero_index[1]], ret.values[ret.zero_index[0]][ret.zero_index[1] - 1] \
                = ret.values[ret.zero_index[0]][ret.zero_index[1] - 1], ret.values[ret.zero_index[0]][ret.zero_index[1]]
            # ustaw odpowiednio pozycje zera
            ret.zero_index[1] -= 1
        elif direction == 'r':
            ret.values[ret.zero_index[0]][ret.zero_index[1]], ret.values[ret.zero_index[0]][ret.zero_index[1] + 1] \
                = ret.values[ret.zero_index[0]][ret.zero_index[1] + 1], ret.values[ret.zero_index[0]][ret.zero_index[1]]
            ret.zero_index[1] += 1
        elif direction == 'u':
            ret.values[ret.zero_index[0]][ret.zero_index[1]], ret.values[ret.zero_index[0] - 1][ret.zero_index[1]] \
                = ret.values[ret.zero_index[0] - 1][ret.zero_index[1]], ret.values[ret.zero_index[0]][ret.zero_index[1]]
            ret.zero_index[0] -= 1
        elif direction == 'd':
            ret.values[ret.zero_index[0]][ret.zero_index[1]], ret.values[ret.zero_index[0] + 1][ret.zero_index[1]] \
                = ret.values[ret.zero_index[0] + 1][ret.zero_index[1]], ret.values[ret.zero_index[0]][ret.zero_index[1]]
            ret.zero_index[0] += 1
        # inkrementuj glebokosc
        ret.depth += 1
        # zapisz ruch
        ret.move_set += direction
        return ret
