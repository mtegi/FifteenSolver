import math
import os
import numpy as np
import matplotlib.pyplot as plt

algorithms = ["astr", "bfs", "dfs"]
search_orders = ["rdul", "rdlu", "drul", "drlu", "ludr", "lurd", "uldr", "ulrd"]
heuristics = ["hamm", "manh"]
levels = [1, 2, 3, 4, 5, 6, 7]
data_categories = ["res_len", "visited_states", "computed_states", "max_depth", "time"]
content = ["data_raw", "mean"]
PUZZLE_DIR = "./puzzles"
OUTPUT_DIR = "./output"
STATISTICS_BFS = "./statistics/bfs"
STATISTICS_ASTR = "./statistics/astr"
STATISTICS_DFS = "./statistics/dfs"
RESULTS_BFS = "./output/bfs"
RESULTS_ASTR = "./output/astr"
RESULTS_DFS = "./output/dfs"


def getFilesDepth(filename):
    return int(filename.split("_")[1])


def printDict(dictionary, title):
    print("**********" + title + "*********")
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
    dictionary = dict.fromkeys(algorithms)
    for algorithm in dictionary:
        dictionary[algorithm] = dict.fromkeys(levels)
        for level in dictionary[algorithm]:
            dictionary[algorithm][level] = dict.fromkeys(data_categories)
            for data_category in dictionary[algorithm][level]:
                dictionary[algorithm][level][data_category] = {}
                dictionary[algorithm][level][data_category]["mean"] = \
                    calculateGeneralMean(dict_dict[algorithm], level, data_category)
    return dictionary


def calculateGeneralMean(dictionary, level, data_category):
    mean_arr = [];
    for strategy in dictionary:
        mean_arr.extend(dictionary[strategy][level][data_category]["data"])
    return np.mean(mean_arr)


def printGeneralDict(dictionary):
    for algorithm in dictionary:
        for level in dictionary[algorithm]:
            for data_category in dictionary[algorithm][level]:
                print("mean for " + str(level) + "|" + algorithm + "|" + data_category)
                print(dictionary[algorithm][level][data_category]["mean"])


def readData(dictionary, datafolder, resultfolder):
    errors = [];
    for strategy in os.listdir(datafolder):
        stat_path = datafolder + "/" + strategy
        result_path = resultfolder + "/" + strategy
        for file in os.listdir(stat_path):
            level = getFilesDepth(file)
            stats_file = open(stat_path + "/" + file, "r")
            result_file = open(result_path + "/" + file, "r")
            if int(result_file.readline()) != -1:
                for data_category in data_categories:
                    if data_category == "time":
                        dictionary[strategy][level][data_category]["data"].append(float(stats_file.readline()))
                    else:
                        dictionary[strategy][level][data_category]["data"].append(int(stats_file.readline()))
            else:
                arr_entry = str(strategy) + "|" + str(file)
                errors.append(arr_entry)
    return errors


def calculateMean(dictionary):
    for strategy in dictionary:
        for level in dictionary[strategy]:
            for data_category in dictionary[strategy][level]:
                dictionary[strategy][level][data_category]["mean"] = \
                    np.mean(dictionary[strategy][level][data_category]["data"])


def createTimePlot(data, title, scale):
    width = 0.1
    plt.grid()
    ind = np.arange(7)
    bar = 1;

    for data_type in data:
        mean_arr = []
        for level in data[data_type]:
            mean_arr.append(data[data_type][level]["time"]["mean"])
        plt.bar(ind + width * bar, mean_arr, width, label=data_type)
        bar += 1

    plt.ylabel("średni czas rozwiązania [ms]")
    plt.xlabel('głębokość rozwiązania')
    plt.title(title)

    plt.xticks(ind + width * bar / 2, levels)
    plt.legend(loc='best')
    plt.yscale(scale)
    plt.savefig('./plots/' + title)
    plt.close()


def createResLenghtPlot(data, title, scale):
    width = 0.1
    plt.grid()
    ind = np.arange(7)
    bar = 1
    max_data = []
    min_data = []

    for data_type in data:
        mean_arr = []
        for level in data[data_type]:
            mean_arr.append(data[data_type][level]["res_len"]["mean"])
        plt.bar(ind + width * bar, mean_arr, width, label=data_type)
        bar += 1
        max_data.append(int(max(mean_arr)))
        min_data.append(int(max(mean_arr)))

    plt.ylabel("średnia długość odnalezionego rozwiązania")
    plt.xlabel('głębokość rozwiązania')
    plt.title(title)
    plt.xticks(ind + width * bar / 2, levels)
    plt.legend(loc='best')
    plt.yscale(scale)
    yint = range(0, math.ceil(max(max_data)) + 1)
    plt.yticks(yint)
    plt.savefig('./plots/' + title)
    plt.close()


def createVisitedPlot(data, title, scale):
    width = 0.1
    plt.grid()
    ind = np.arange(7)
    bar = 1
    max_data = []
    min_data = []

    for data_type in data:
        mean_arr = []
        for level in data[data_type]:
            mean_arr.append(data[data_type][level]["visited_states"]["mean"])
        plt.bar(ind + width * bar, mean_arr, width, label=data_type)
        bar += 1
        max_data.append(int(max(mean_arr)))
        min_data.append(int(max(mean_arr)))

    plt.ylabel("Średnia liczba stanów odwiedzonych")
    plt.xlabel('głębokość rozwiązania')
    plt.title(title)
    plt.xticks(ind + width * bar / 2, levels)
    plt.legend(loc='best')
    plt.yscale(scale)
    plt.savefig('./plots/' + title)
    plt.close()


def createComputedPlot(data, title, scale):
    width = 0.1
    plt.grid()
    ind = np.arange(7)
    bar = 1
    max_data = []
    min_data = []

    for data_type in data:
        mean_arr = []
        for level in data[data_type]:
            mean_arr.append(data[data_type][level]["computed_states"]["mean"])
        plt.bar(ind + width * bar, mean_arr, width, label=data_type)
        bar += 1
        max_data.append(int(max(mean_arr)))
        min_data.append(int(max(mean_arr)))

    plt.ylabel("Średnia liczba stanów przetworzonych")
    plt.xlabel('głębokość rozwiązania')
    plt.title(title)
    plt.xticks(ind + width * bar / 2, levels)
    plt.legend(loc='best')
    plt.yscale(scale)
    plt.savefig('./plots/' + title)
    plt.close()


def createMaxDepthPlot(data, title, scale):
    width = 0.1
    plt.grid()
    ind = np.arange(7)
    bar = 1
    max_data = []
    min_data = []

    for data_type in data:
        mean_arr = []
        for level in data[data_type]:
            mean_arr.append(data[data_type][level]["max_depth"]["mean"])
        plt.bar(ind + width * bar, mean_arr, width, label=data_type)
        bar += 1
        max_data.append(int(max(mean_arr)))
        min_data.append(int(max(mean_arr)))

    plt.ylabel("Średnia maksymalnie osiągnięta głębokość")
    plt.xlabel('głębokość rozwiązania')
    plt.title(title)
    plt.xticks(ind + width * bar / 2, levels)
    plt.legend(loc='best')
    yint = range(0, math.ceil(max(max_data)) + 1)
    plt.yscale(scale)
    plt.yticks(yint)
    plt.savefig('./plots/' + title)
    plt.close()


bfs = createDictionary(search_orders)
readData(bfs, STATISTICS_BFS, RESULTS_BFS)
calculateMean(bfs)
printDict(bfs, "BFS")

dfs = createDictionary(search_orders)
dfs_err = readData(dfs, STATISTICS_DFS, RESULTS_DFS)
calculateMean(dfs)
printDict(dfs, "DFS")

astr = createDictionary(heuristics)
readData(astr, STATISTICS_ASTR, RESULTS_ASTR)
calculateMean(astr)
printDict(astr, "ASTR")

masterDict = {"bfs": bfs, "astr": astr, "dfs": dfs}

generalDict = createGeneralDictionary(masterDict)
printGeneralDict(generalDict)

print(dfs_err)
print(dfs_err.__len__())

createTimePlot(generalDict, "Czas rozwiązania - wszystkie algorytmy", 'log')
createTimePlot(bfs, "Czas rozwiązania - bfs", 'linear')
createTimePlot(dfs, "Czas rozwiązania - dfs", 'log')
createTimePlot(astr, "Czas rozwiązania - astr", 'linear')

createResLenghtPlot(bfs, "długość rozwiązania - bfs", 'linear')
createResLenghtPlot(dfs, "długość rozwiązania - dfs", 'linear')
createResLenghtPlot(astr, "długość rozwiązania - astr", 'linear')
createResLenghtPlot(generalDict, "długość rozwiązania - wszystkie algorytmy", 'linear')

createVisitedPlot(bfs, "liczba stanów odwiedzonych - bfs", 'linear')
createVisitedPlot(dfs, "liczba stanów odwiedzonych - dfs", 'log')
createVisitedPlot(astr, "liczba stanów odwiedzonych - astr", 'linear')
createVisitedPlot(generalDict, "liczba stanów odwiedzonych - wszystkie algorytmy", 'log')

createComputedPlot(bfs, "liczba stanów przetworzonych - bfs", 'linear')
createComputedPlot(dfs, "liczba stanów przetworzonych - dfs", 'log')
createComputedPlot(astr, "liczba stanów przetworzonych - astr", 'linear')
createComputedPlot(generalDict, "liczba stanów przetworzonych - wszystkie algorytmy", 'log')

createMaxDepthPlot(bfs, "maksymalna osiągnięta głębokość - bfs", 'linear')
createMaxDepthPlot(dfs, "maksymalna osiągnięta głębokość - dfs", 'linear')
createMaxDepthPlot(astr, "maksymalna osiągnięta głębokość - astr", 'linear')
createMaxDepthPlot(generalDict, "maksymalna osiągnięta głębokość - wszystkie algorytmy", 'linear')
