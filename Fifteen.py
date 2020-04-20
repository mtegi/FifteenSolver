import sys
import re
from timeit import default_timer as timer
from typing import Tuple

from BFS import BFS
from DFS import DFS
from State import State
import numpy as np


def index(array: np.ndarray, item: int) -> Tuple[int, int]:
    for idx, val in np.ndenumerate(array):
        if val == item:
            return idx


def solve(args):
    algo = str(args[0])
    param = str(args[1]).lower()
    input_file = str(args[2])
    output_file = str(args[3])
    stats_file = str(args[4])
    data = read_state_from_file(input_file)
    height = data[0]
    width = data[1]
    values = np.reshape(np.array(data[2:]), (height, width,))
    init_state = State(height, width, values, index(values, 0), 1, "")
    result = None
    start_time = 0
    end_time = 0
    if algo == 'bfs':
        bfs = BFS(init_state, param)
        start_time = timer()
        result = bfs.find_solution()
        end_time = timer()
    elif algo == 'dfs':
        dfs = DFS(init_state, param)
        start_time = timer()
        result = dfs.find_solution()
        end_time = timer()
    elif algo == 'astr':
        print()
    else:
        print('Wrong algorithm')
    save_to_file(output_file, stats_file, result, get_time(start_time, end_time))


def get_time(start: float, end: float) -> float:
    time_in_seconds = end - start
    return round(time_in_seconds * 1000, 3)


def read_state_from_file(file: str):
    f = open(file, 'r')
    data = re.split(' |\n', f.read())
    if data[-1] == '':
        data.remove(data[-1])
    f.close()
    return [int(i) for i in data]


def save_to_file(result_file: str, stats_file: str, result: Tuple[str, int, int, int], time_lapsed: float) -> None:
    f = open(result_file, 'w')
    f.write("".join([str(len(result[0])), '\n', result[0]]))
    f.close()
    f = open(stats_file, 'w')
    concat = [str(len(result[0])), '\n', str(result[2]), '\n', str(result[2]), '\n',
              str(result[3]), '\n', str(result[1]), '\n', str(time_lapsed)]
    f.write("".join(concat))
    f.close()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print('Bledne argsy')
    else:
        solve(sys.argv[1:6])
