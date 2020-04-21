import os
import matplotlib.pyplot as plt

search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]
PUZZLE_DIR = "./puzzles"
OUTPUT_DIR = "./output"
STATISTICS_DIR = "./statistics"

data = {}


def read_file(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    return int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3]), int(lines[4]), float(lines[5])


def read_data():
    values = []
    for o in search_orders:
        files = [f for f in os.listdir("".join([STATISTICS_DIR, '/', o])) if f.endswith(".txt")]
        for f in files:
            values.append(read_file("".join([STATISTICS_DIR, '/', o, '/', f])))
        data[o] = values


read_data()
print('done')
