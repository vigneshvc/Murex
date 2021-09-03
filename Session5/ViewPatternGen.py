import json
import os
import multiprocessing as mp


def readDataFromJsonFile(fileName):
    f = open(fileName, 'r')
    data = json.load(f)
    lst = []
    op = []
    lst.append(fileName[:-14])
    lst.append(list(data['Unique_Column'].keys()))
    b = False
    for k, v in data.items():
        if b:
            op = op + [lst.copy() + [k] + dt + [data['Check_instance']['Events']]
                       for dt in list(map(list, v.items()))]
        b = b or k == 'Grouping_Column'
    return op


if __name__ == "__main__":
    pool = mp.Pool(processes=mp.cpu_count())
    path_to_json = os.path.dirname(os.path.realpath(__file__))
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('_patterns.json')]
    resultList = sum(pool.map(readDataFromJsonFile, json_files), [])
    pool.close()
    pool.join()
    print(resultList)
