from Fifteen import Fifteen
from pathlib import Path
import os

search_orders = ["rdul","rdlu","drul","drlu","ludr","lurd","uldr","ulrd"]

for o in search_orders:
    Path("./output/" + o).mkdir(parents=True, exist_ok=True)
    Path("./statistics/" + o).mkdir(parents=True, exist_ok=True)

for file in os.listdir("./puzzles"):
    if file.endswith(".txt"):
        for o in search_orders:
            out = "./output/" + o + '/' + file
            stat = "./statistics/" + o + '/' + file
            Fifteen(["bfs", o, "./puzzles/" + file, out, stat])
