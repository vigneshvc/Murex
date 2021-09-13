import os

for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue

'''

Level1 = 'User Name'
Level2 = 'User Group'
Level3 = 'User Desk'
Level4 = ['Counterparty', 'Internal/External', 'Trade Status', 'Portfolio', 'Clearing Eligibility', 'Typology', 'Source System', 'Entity', 'Trade Insert', 'Flow Currency', 'Last Contract Event Action', 'Payment Netting', 'Contract Id', 'Party Name', 'partyName2']
FileData = pd.read_csv("murex_demo.csv") # Pandas DataFrame
CumulativeData = dict()# Key,value pair
for label, dataRows in FileData.iterrows():
    level123 = list()
    level123.append(dataRows[Level1])
    level123.append(dataRows[Level2])
    level123.append(dataRows[Level3])
    for i in Level4:
        row = list()
        row.extend(level123)
        row.append(i) #Level4
        row.append(dataRows[i]) #Level5
        # row = list of Level1-5
        if tuple(row) in CumulativeData:
            CumulativeData[tuple(row)] += 1
        else:
            CumulativeData[tuple(row)] = 1
FinalData = []
for key,value in CumulativeData.items():
    FinalData.append(key+(value,))
murex_demo_calculated = pd.DataFrame(FinalData, columns = LevelNames)
murex_demo_calculated.to_csv('murex_demo_calculated.csv', index=False)



#fileData = fileData.groupby(fileData.columns.tolist()).apply(len).rename('count').reset_index().sort_values(by = LevelNames[::-1], ascending = False)


fileData = pd.read_csv("murex_demo.csv").set_index(['User Name','User Group','User Desk']).stack().to_frame().reset_index()
fileData.columns = ['Level1','Level2','Level3','Level4','Level5']
fileData = fileData.groupby(['Level1','Level2','Level3','Level4','Level5']).size().reset_index().rename(columns = {0:'Count'})
print(fileData)
fileData.to_csv('testcsv.csv',index=False)

index
column
set_index -> column to index
DataFrame.loc[[index],[columns]] ':'->all
reset_index -> all indices to column
stack-> convert all column to a single index with values as single column
to_frame() converts other panda datatypes to DataFrame
groupby() accepts list of columns and group them -> returns groupby. Other aggregate functions must be called
size -> returns number of rows in each groups as seperate column
rename() -> used to rename column/index
to_csv -> converts DataFrame to csv file
'''
