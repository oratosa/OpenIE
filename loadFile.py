# %%
import os,glob
import pandas as pd
from email.parser import Parser

# %%
def getDirList(directory_path:str) -> list:
    if os.path.isdir(directory_path) == True:
        directory_path = directory_path + '/**'
        path_list = glob.glob(directory_path, recursive=True)
        dir_list = []
        for path in path_list:
            if os.path.isdir(path) == True:
                dir_list.append(path)
        return dir_list
    else:
        print("{} is not a directory path.".format(directory_path))

def getFileList(directory_path:str) -> list:
    if os.path.isdir(directory_path) == True:
        directory_path = directory_path + '/**'
        path_list = glob.glob(directory_path, recursive=True)
        file_list = []
        for path in path_list:
            if os.path.isfile(path) == True:
                file_list.append(path)
        return file_list
    else:
        print("{} is not a directory path.".format(directory_path))

def fileToDataFrame(file_list:list) -> pd.DataFrame:
    cols = ['Path', 'Message-ID', 'Date', 'From', 'To', 'Cc', 'Bcc', 'X-From', 'X-To', 'X-cc', 'X-bcc', 'Subject', 'Message']
    df = pd.DataFrame(index=[], columns=cols)
    
    for file in file_list:
        with open(file) as f:
            mail = Parser().parse(f)
        record = {}
        for header in cols:
            if header == 'Path':
                record[header] = file
            elif header == 'Message':
                record[header] = mail.get_payload()
            else:
                record[header]=mail.get(header)
        df = df.append(record, ignore_index=True)
    return df

# %%
