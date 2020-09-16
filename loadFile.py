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
    mail_cols = ['file_path','message_id','from','date','in_reply_to','references''subject','body']
    
    mail_df = pd.DataFrame(index=[], columns=mail_cols)
    
    for file in file_list:
        with open(file) as f:
            mail = Parser().parse(f)

        record = {}
        for col in mail_cols:
            if col == 'file_path':
                record[col] = file
            elif col == 'body':
                record[col] = mail.get_payload()
            else:
                record[col] = mail.get(col)
        mail_df = mail_df.append(record, ignore_index=True)
    
    return mail_df
