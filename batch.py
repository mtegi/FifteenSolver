import multiprocessing
import time
from Fifteen import Fifteen
from pathlib import Path
import os

search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]


def make_dirs():
    for o in search_orders:
        Path("./output/" + o).mkdir(parents=True, exist_ok=True)
        Path("./statistics/" + o).mkdir(parents=True, exist_ok=True)


def calc(file):
    for o in search_orders:
        out = "./output/" + o + '/' + file
        stat = "./statistics/" + o + '/' + file
        Fifteen(["bfs", o, "./puzzles/" + file, out, stat])


if __name__ == '__main__':
    make_dirs()
    start = time.time()
    print("Running script...")
    files = [f for f in os.listdir("./puzzles") if f.endswith(".txt")]
    pool = multiprocessing.Pool()
    pool.map(calc, files)
    pool.close()
    print('Time: {} sec '.format(time.time() - start))

