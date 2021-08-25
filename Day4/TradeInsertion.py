import json
f = open('dendo_patterns.json', 'r')
data = json.load(f)
imperative_name = 'TradeInsertion'
print(type(data))
unique_column = 'portfolio'
for key, value in data[imperative_name].items():
    if key == 'Unique_Column' :
        pass