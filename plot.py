import os
import numpy as np
import matplotlib.pyplot as plt

algorithms = ["astr", "bfs"]
search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]
heuristics = ["hamm", "manh"]
levels = [1, 2, 3, 4, 5, 6, 7]
data_categories = ["res_len", "visited_states", "computed_states", "max_depth", "time"]
content = ["data_raw", "mean"]
PUZZLE_DIR = "./puzzles"
OUTPUT_DIR = "./output"
STATISTICS_BFS = "./statistics/bfs"
STATISTICS_ASTR = "./statistics/astr"


def getFilesDepth(filename):
    return int(filename.split("_")[1])


def printDict(dictionary):
    for strategy in dictionary:
        print("@Data for strategy: " + strategy)
        for level in dictionary[strategy]:
            print("###level...: " + str(level))
            for data_category in dictionary[strategy][level]:
                print("---category data...: " + data_category)
                print(dictionary[strategy][level][data_category]["data"])
                print("---mean...: " + data_category)
                print(dictionary[strategy][level][data_category]["mean"])


def createDictionary(strategies):
    dictionary = dict.fromkeys(strategies)
    for strategy in dictionary:
        dictionary[strategy] = dict.fromkeys(levels)
        for level in dictionary[strategy]:
            dictionary[strategy][level] = dict.fromkeys(data_categories)
            for data_category in dictionary[strategy][level]:
                dictionary[strategy][level][data_category] = dict.fromkeys(["data", "mean"])
                dictionary[strategy][level][data_category]["data"] = []
    return dictionary


def createGeneralDictionary(dict_dict):
    dictionary = dict.fromkeys(levels)
    for level in dictionary:
        dictionary[level] = dict.fromkeys(algorithms)
        for algorithm in dictionary[level]:
            dictionary[level][algorithm] = dict.fromkeys(data_categories)
            for data_category in dictionary[level][algorithm]:
                dictionary[level][algorithm][data_category] = \
                    calculateGeneralMean(dict_dict[algorithm], level, data_category)
    return dictionary


def calculateGeneralMean(dictionary, level, data_category):
    mean_arr = [];
    for strategy in dictionary:
        mean_arr.extend(dictionary[strategy][level][data_category]["data"])
    return np.mean(mean_arr)


def printGeneralDict(dictionary):
    for level in dictionary:
        for algorithm in dictionary[level]:
            for data_category in dictionary[level][algorithm]:
                print("mean for " + str(level) + "|" + algorithm + "|" + data_category)
                print(dictionary[level][algorithm][data_category])


def readData(dictionary, datafolder):
    for strategy in os.listdir(datafolder):
        path = datafolder + "/" + strategy
        for file in os.listdir(path):
            level = getFilesDepth(file)
            open_file = open(path + "/" + file, "r")
            for data_category in data_categories:
                if data_category == "time":
                    dictionary[strategy][level][data_category]["data"].append(float(open_file.readline()))
                else:
                    dictionary[strategy][level][data_category]["data"].append(int(open_file.readline()))


def calculateMean(dictionary):
    for strategy in dictionary:
        for level in dictionary[strategy]:
            for data_category in dictionary[strategy][level]:
                dictionary[strategy][level][data_category]["mean"] = \
                    np.mean(dictionary[strategy][level][data_category]["data"])


bfs = createDictionary(search_orders)
readData(bfs, STATISTICS_BFS)
calculateMean(bfs)
printDict(bfs)

astr = createDictionary(heuristics)
readData(astr, STATISTICS_ASTR)
calculateMean(astr)
printDict(astr)

masterDict = {"bfs": bfs, "astr": astr}

generalDict = createGeneralDictionary(masterDict)
printGeneralDict(generalDict)

# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Frank')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Guido')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D'))
plt.legend()

plt.tight_layout()
plt.show()
