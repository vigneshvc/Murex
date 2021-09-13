import json
import os
import xml.etree.ElementTree as ET

import pandas as pd

resultList = []
f = open('sample.json', 'r')
data = json.load(f)
path = r"mxdev21_trade_xmls_set1"
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
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
    resultList.append(y)
# print(resultList)
fields = []
for key, value in data['common_tags'].items():
    fields.append(key)
# print(fields)
fileData = pd.DataFrame(resultList, columns=fields)
fileData.to_csv('murex_trade.csv', index=False)

fileData = pd.read_csv("murex_trade.csv")
fileData = fileData.set_index(['User Name', 'User Group', 'User Desk'])
print(fileData.head().to_string())
fileData = fileData.stack().to_frame().reset_index()
print(fileData.head().to_string())
fileData.columns = ['Level1', 'Level2', 'Level3', 'Level4', 'Level5']
fileData = fileData.groupby(['Level1', 'Level2', 'Level3', 'Level4', 'Level5']).size().reset_index().rename(
    columns={0: 'Count'})
fileData.to_csv('murex_trade_calculated.csv', index=False)
