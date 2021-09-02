import pandas as pd
import os
import itertools
import string


def get_dataframe(input_file_name):
    if os.path.isfile(input_file_name+'.csv'):
        print("Fetching data from csv file")
        ddf = pd.read_csv(input_file_name+'.csv')
        print("Data fetched")
        return ddf
    df = pd.read_excel(input_file_name+'.xlsx')
    print("Fetching data from excel file")
    df.to_csv(input_file_name+'.csv', index=False)
    print("Data fetched and csv file is also generated")
    return df


def gen_seq():
    try:
        gen_seq.i += 1
    except AttributeError:
        gen_seq.seq = []
        for size in [1,2,3,4]:
            for s in itertools.product(string.ascii_uppercase, repeat=size):
                gen_seq.seq.append("".join(s))
        gen_seq.i = 0
    return "Type "+gen_seq.seq[gen_seq.i]

try:
    input_file_name = "OSP_Rabo_20Apr"
    output_file_name = "OSP"
    fileData = get_dataframe(input_file_name)
    print("Processing Data...")
    fileData = fileData.sort_values(by='ENTRY TIME')
    fileData = fileData.loc[:, ['TYPOLOGY', 'OSP_QUEUE_NAME', 'FROM_TASK', 'TO_TASK', 'CONTRACT_ID']]
    fileData = fileData.groupby(fileData.columns.to_list()).size().reset_index().rename(columns={0: 'Count'})
    columnList = fileData.columns.to_list()
    columnList.remove('CONTRACT_ID')
    fileData.set_index(columnList, inplace=True)
    fileData = fileData.groupby('CONTRACT_ID').apply(lambda x: pd.Series(gen_seq(), x.index)).reset_index().rename(
        columns={0: 'Level2', 'TYPOLOGY': 'Level1', 'OSP_QUEUE_NAME': 'Level3', 'FROM_TASK': 'Level4',
                 'TO_TASK': 'Level5'}).drop('CONTRACT_ID', axis=1)[
        ['Level1', 'Level2', 'Level3', 'Level4', 'Level5', 'Count']]
    print("Data processed. Exporting to csv...")
    fileData.to_csv(output_file_name+'.csv', index=False)
    print("CSV file is generated : "+output_file_name+".csv")
except PermissionError:
    print("CSV file cannot be generated. Kindly close the file and try again")
except Exception:
    print("Error occured. Processing failed")