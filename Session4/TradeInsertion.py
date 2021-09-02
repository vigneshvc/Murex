import json


def getDictContent(content1, unique_column1):
    fnd =list()
    for k, v in content1.items():
        if type(v) == dict:
            fnd.extend(getDictContent(v,unique_column1))
        else:
            if k==unique_column1:
                fnd.append(v)
    return fnd


def updateUniqueColumn(content, unique_column):
    if unique_column in content['Unique_Column'].keys():
        return content
    content['Unique_Column'][unique_column] = getDictContent(content,unique_column)
    return content



filename = 'dendo_patterns.json'
f = open(filename, 'r')
data = json.load(f)
imperative_name = 'TradeInsertion'
unique_column = 'Portfolio'
data[imperative_name]['Unique_Column'] = unique_column
with open(filename, 'w') as outfile:
    outfile.write(json.dumps(data,indent=4))
f = open(data[imperative_name]['Sub_Type'] + '_patterns.json', 'r')
content = json.load(f)
content = updateUniqueColumn(content, unique_column)
with open(data[imperative_name]['Sub_Type'] + '_patterns.json', 'w') as outfile:
    outfile.write(json.dumps(content, indent=4))
