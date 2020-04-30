import multiprocessing
import time
from functools import partial

from Fifteen import solve
from pathlib import Path
import os

search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]
heuristics = ["manh", "hamm"]
PUZZLE_DIR = "./puzzles"
OUTPUT_DIR = "./output"
STATISTICS_DIR = "./statistics"
algorithms = ["bfs", "dfs"]


def make_dirs() -> None:
    for a in algorithms:
        for o in search_orders:
            Path("".join([OUTPUT_DIR, '/', a, '/', o])).mkdir(parents=True, exist_ok=True)
            Path("".join([STATISTICS_DIR, '/', a, '/', o])).mkdir(parents=True, exist_ok=True)
    for h in heuristics:
        Path("".join([OUTPUT_DIR, '/', 'astr', '/', h])).mkdir(parents=True, exist_ok=True)
        Path("".join([STATISTICS_DIR, '/', 'astr', '/', h])).mkdir(parents=True, exist_ok=True)


def calc(algo: str, file: str) -> None:
    for o in search_orders:
        out = "".join([OUTPUT_DIR, '/', algo, '/', o, '/', file])
        stat = "".join([STATISTICS_DIR, '/', algo, '/', o, '/', file])
        in_ = "".join([PUZZLE_DIR, '/', file])
        solve([algo, o, in_, out, stat])


def calcAstr(algo: str, file: str) -> None:
    for h in heuristics:
        out = "".join([OUTPUT_DIR, '/', algo, '/', h, '/', file])
        stat = "".join([STATISTICS_DIR, '/', algo, '/', h, '/', file])
        in_ = "".join([PUZZLE_DIR, '/', file])
        solve([algo, h, in_, out, stat])


if __name__ == '__main__':
    make_dirs()
    print("Starting...")
    files = [f for f in os.listdir(PUZZLE_DIR) if f.endswith(".txt")]
    print("Doing A*")
    start = time.time()
    pool = multiprocessing.Pool()
    pool.map(partial(calcAstr, "astr"), files)
    pool.close()
    print('Time: {} sec '.format(time.time() - start))
    for a in algorithms:
        print("".join(['Doing ', a]))
        start = time.time()
        pool = multiprocessing.Pool()
        pool.map(partial(calc, a), files)
        pool.close()
        print('Time: {} sec '.format(time.time() - start))
    exit(0)
