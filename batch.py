import multiprocessing
import time
from Fifteen import Fifteen
from pathlib import Path
import os

search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]
PUZZLE_DIR = "./puzzles"
OUTPUT_DIR = "./output"
STATISTICS_DIR = "./statistics"


def make_dirs() -> None:
    for o in search_orders:
        Path("".join([OUTPUT_DIR, '/', o])).mkdir(parents=True, exist_ok=True)
        Path("".join([STATISTICS_DIR, '/', o])).mkdir(parents=True, exist_ok=True)


def calc(file: str) -> None:
    for o in search_orders:
        out = "".join([OUTPUT_DIR, '/', o, '/', file])
        stat = "".join([STATISTICS_DIR, '/', o, '/', file])
        in_ = "".join([PUZZLE_DIR, '/', file])
        Fifteen(["bfs", o, in_, out, stat])


if __name__ == '__main__':
    make_dirs()
    start = time.time()
    print("Running script...")
    files = [f for f in os.listdir(PUZZLE_DIR) if f.endswith(".txt")]
    pool = multiprocessing.Pool()
    pool.map(calc, files)
    pool.close()
    print('Time: {} sec '.format(time.time() - start))

