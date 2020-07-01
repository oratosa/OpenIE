import pandas as pd
from email.parser import Parser

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
