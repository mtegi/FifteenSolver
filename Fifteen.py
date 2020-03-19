import sys
import re
import datetime
from BFS import BFS
from DFS import DFS
from State import State


class Fifteen:
    def __init__(self, args):
        # algorytm
        self.algo = str(args[0])
        # kolejnosc przeszukiwania / heurystyka
        self.param = str(args[1]).lower()
        # plik z ukladanka
        self.input = str(args[2])
        # plik z rozwiazaniem
        self.output = str(args[3])
        # plik z informacjami dodatkowymi
        self.stats = str(args[4])
        self.solve()

    # rozwiaz ukladanke
    def solve(self):
        init_state = State(read_state_from_file(self.input))
        if self.algo == 'bfs':
            bfs = BFS(init_state, self.param)
            start_time = datetime.datetime.now()
            result = bfs.find_solution()
            end_time = datetime.datetime.now()
            save_to_file(self.output, self.stats, result, start_time, end_time)
        elif self.algo == 'dfs':
            dfs = DFS(init_state, self.param)
            start_time = datetime.datetime.now()
            result = dfs.find_solution()
            end_time = datetime.datetime.now()
            save_to_file(self.output, self.stats, result, start_time, end_time)
        elif self.algo == 'astr':
            print()
        else:
            print('Wrong algorithm')


# wczytaj stan z pliku
def read_state_from_file(file):
    f = open(file, 'r')
    data = re.split(' |\n', f.read())
    f.close()
    return [int(i) for i in data]


# zapisz wyniki
def save_to_file(result_file, stats_file, result, start_time, end_time):
    f = open(result_file, 'w')
    f.write(len(result[0]).__str__() + '\n')
    f.write(result[0])
    f.close()
    f = open(stats_file, 'w')
    time_lapsed = end_time - start_time
    f.write(len(result[0]).__str__() + '\n' + result[2].__str__() +
            '\n' + result[3].__str__() + '\n' + result[1].__str__() + '\n' + time_lapsed.__str__())
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print('Bledne argsy')
    else:
        Fifteen(sys.argv[1:6])
