import xml.etree.ElementTree as ET
import json
import pandas as pd
import os



f = open(r'sample.json', 'r')
data = json.load(f)
#print(data)
path = r"mxdev21_trade_xmls_set4"

resultList = []
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
    fullname=os.path.join(path,filename)
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
print(resultList)
fields = []
for key in data['common_tags'].keys():
    fields.append(key)

#print(",".join(fields))
murex_demo = pd.DataFrame(resultList, columns=fields)
murex_demo.to_csv('murex_demo.csv',index=False)






