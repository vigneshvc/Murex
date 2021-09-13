import xml.etree.ElementTree as ET
import json
import pandas as pd
import os
import time
import multiprocessing as mp


def extract_from_xml(filename):
    fullname = os.path.join(path, filename)
    mytree = ET.parse(fullname)
    root = mytree.getroot()
    myroot = ET.Element("root")
    myroot.insert(0, root)
    y = []
    for key, value in data['common_tags'].items():
        t = myroot.findall(value)
        if len(t) == 0:
            y.append("None")
            continue
        y.append(t[0].text)
    return y


resultList = []
f = open('sample.json', 'r')
data = json.load(f)
path = r"mxdev21_trade_xmls_set1"
if __name__ == "__main__":
    pool = mp.Pool(processes=mp.cpu_count())
    print("Starting to extract data from xml files")
    start = time.time()
    resultList = pool.map(extract_from_xml, os.listdir(path))
    pool.close()
    pool.join()
    end = time.time()
    print("Data extracted from xml files - Time elapsed :", round(end - start, 2), "seconds")
    fields = []
    for key, value in data['common_tags'].items():
        fields.append(key)
    murex_demo = pd.DataFrame(resultList, columns=fields)
    murex_demo.to_csv('murex_trade.csv', index=False)
    print("Processing Data...")
    fileData = pd.read_csv("murex_trade.csv")
    fileData = fileData.set_index(['User Name', 'User Group', 'User Desk'])
    fileData = fileData.stack().to_frame().reset_index()
    # print(fileData)
    fileData.columns = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5']
    fileData = fileData.groupby(['Level1', 'Level2', 'Level3', 'Level4', 'Level5']).size().reset_index().rename(
        columns={0: 'Count'})
    fileData.to_csv('murex_trade_calculated.csv', index=False)
    print("Data processed : murex_trade_calculated.csv")
    print("Total time taken :",round(time.time() - start,2),"seconds")
