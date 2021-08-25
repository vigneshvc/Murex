import json

f = open('dendo_patterns.json', 'r')
data = json.load(f)
imperative_name = 'TradeInsertion'
print(data)
unique_column = 'portfolio'
data[imperative_name]['Unique_Column'] = unique_column
if 'Unique_Column' in data[imperative_name].keys():
    print('Unique_Column is found')
else:
    print("Unique_Column is not found")
    data[imperative_name]['Unique_Column'] = unique_column
print(data)
for key, value in data[imperative_name].items():
    if key == 'Unique_Column':
        pass
