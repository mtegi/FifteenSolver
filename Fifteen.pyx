import re
from timeit import default_timer as timer
from typing import Tuple

import numpy as np

from AStar import AStar
from BFS import BFS
from DFS import DFS
from State import State

def index(array: np.ndarray, item: int) -> Tuple[int, int]:
    for idx, val in np.ndenumerate(array):
        if val == item:
            return idx


cpdef solve(args):

    cdef str algo = str(args[0])
    cdef str param = str(args[1]).lower()
    cdef str input_file = str(args[2])
    cdef str output_file = str(args[3])
    cdef str stats_file = str(args[4])
    data = read_state_from_file(input_file)
    cdef int height = data[0]
    cdef int width = data[1]
    values = np.reshape(np.array(data[2:]), (height, width,))
    init_state = State(height, width, values, index(values, 0), 1, "")
    result = None
    cdef float start_time = 0
    cdef float end_time = 0
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
        astr = AStar(init_state, param)
        start_time = timer()
        result = astr.find_solution()
        end_time = timer()
    else:
        print('Wrong algorithm')

    if result is None:
        f = open(output_file, 'w')
        f.write("-1")
        f.close()
        f = open(stats_file, 'w')
        f.write("-1")
        f.close()
    else:
        save_to_file(output_file, stats_file, result, get_time(start_time, end_time))



cdef float get_time(float start, float end):
    time_in_seconds = end - start
    return time_in_seconds * 1000


cpdef read_state_from_file(str file):
    f = open(file, 'r')
    data = re.split(' |\n', f.read())
    if data[-1] == '':
        data.remove(data[-1])
    f.close()
    return [int(i) for i in data]


cpdef save_to_file(result_file: str, stats_file: str, result: Tuple[str, int, int, int], time_lapsed: float):
    f = open(result_file, 'w')
    f.write("".join([str(len(result[0])), '\n', result[0]]))
    f.close()
    f = open(stats_file, 'w')
    concat = [str(len(result[0])), '\n', str(result[2]), '\n',
              str(result[3]), '\n', str(result[1]), '\n', format(time_lapsed,'.3f')]
    f.write("".join(concat))
    f.close()



