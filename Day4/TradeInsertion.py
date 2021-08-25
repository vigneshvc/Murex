import json

def getDictContent(content,unique_column):
    for k,v in content.items():
        if k == unique_column:
            yield str(v)
        if type(v) == type(dict()):
            yield getDictContent(v,unique_column)
def updateUniqueColumn(content,unique_column):
    for foundItems in getDictContent(content,unique_column):
        print(foundItems)
    return content

filename = 'dendo_patterns.json'
f = open(filename, 'r')
data = json.load(f)
imperative_name = 'TradeInsertion'
print(data)
unique_column = 'portfolio'
data[imperative_name]['Unique_Column'] = unique_column
with open(filename,'w') as outfile:
    json.dump(data,outfile)
f = open(data[imperative_name]['Sub_Type']+'_patterns.json','r')
content = json.load(f)
content = updateUniqueColumn(content,unique_column)
