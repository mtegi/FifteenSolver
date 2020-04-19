import sys
import re
from timeit import default_timer as timer
from BFS import BFS
from DFS import DFS
from State import State


class Fifteen:
    def __init__(self, args):
        self.algo = str(args[0])
        self.param = str(args[1]).lower()
        self.input = str(args[2])
        self.output = str(args[3])
        self.stats = str(args[4])
        self.solve()

    # rozwiaz ukladanke
    def solve(self):
        init_state = State(read_state_from_file(self.input))
        if self.algo == 'bfs':
            bfs = BFS(init_state, self.param)
            start_time = timer()
            result = bfs.find_solution()
            end_time = timer()
            save_to_file(self.output, self.stats, result, get_time(start_time, end_time))
        elif self.algo == 'dfs':
            dfs = DFS(init_state, self.param)
            start_time = timer()
            result = dfs.find_solution()
            end_time = timer()
            save_to_file(self.output, self.stats, result, get_time(start_time, end_time))
        elif self.algo == 'astr':
            print()
        else:
            print('Wrong algorithm')


def get_time(start, end):
    time_in_seconds = end - start
    return round(time_in_seconds * 1000, 3)


# wczytaj stan z pliku
def read_state_from_file(file):
    f = open(file, 'r')
    data = re.split(' |\n', f.read())
    if data[-1] == '':
        data.remove(data[-1])
    f.close()
    return [int(i) for i in data]


# zapisz wyniki
def save_to_file(result_file, stats_file, result, time_lapsed):
    f = open(result_file, 'w')
    f.write(len(result[0]).__str__() + '\n')
    f.write(result[0])
    f.close()
    f = open(stats_file, 'w')
    f.write(len(result[0]).__str__() + '\n' + result[2].__str__() +
            '\n' + result[3].__str__() + '\n' + result[1].__str__() + '\n' + time_lapsed.__str__())
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print('Bledne argsy')
    else:
        Fifteen(sys.argv[1:6])
