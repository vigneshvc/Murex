'''

open folder
for all files -> *_patterns.json
Subtype - > Filename -> "".rstrip('_')
open file
uniqueness-> 'Unique_Column' -> keys
For all keys under the key -> 'Grouping Column' -->> Typology -> keys
under all typology -> if value != {} -> all keys are 'header' and values are 'path'
Check instance -> 'Events' -> value is Ordinal

List op format -> [[subtype, [uniqueness], typology , header , path , ordinal],[],...]


'''

import json
import os
import time
import multiprocessing as mp


def readDataFromJsonFile(fileName):
    f = open(fileName, 'r')
    data = json.load(f)
    lst = []
    op = []
    lst.append(fileName[:-14])  # subtype
    lst.append(list(data['Unique_Column'].keys()))  # uniqueness
    print(lst)
    b = False
    for k, v in data.items():
        b = b or k == 'Grouping_Column'
        if b and not k == 'Grouping_Column':
            op = op + [lst.copy() + [k] + dt + [data['Check_instance']['Events']]
                    for dt in list(map(list, data[k].items())) if type(data[k]) == dict]
    return op
if __name__ == "__main__":
    pool = mp.Pool(processes=mp.cpu_count())
    path_to_json = os.path.dirname(os.path.realpath(__file__))
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('_patterns.json')]
    print(json_files)
    start = time.time()
    #resultList = []
    resultList = sum(pool.map(readDataFromJsonFile,json_files), [])
    #for i in json_files:
    #    resultList += readDataFromJsonFile(i)
    pool.close()
    pool.join()
    end = time.time()
    print("Data extracted from json files - Time elapsed :", round(end - start, 2), "seconds")
    print(resultList)
