#%%
from email.parser import Parser
with open("wiki-research-l/2020-July/2020-July-00") as f:
    mail = Parser().parse(f)

# %%
# メールのヘッダー情報を処理する
import pandas as pd 

mail_cols = ['file_path','Message-ID','From','Date','Subject','Content']
thread_cols = ['file_path','Message-ID','In-Reply-To','References']

mail_df = pd.DataFrame(index=[], columns=mail_cols)
thread_df = pd.DataFrame(index=[], columns=thread_cols)

file_path = '2020-July-00'

# mail_df
record = {}
for col in mail_cols:
    if col == 'file_path':
        record[col] = file_path
    elif col == 'Content':
        record[col] = mail.get_payload()
    else:
        record[col] = mail.get(col)
mail_df = mail_df.append(record, ignore_index=True)

# thread_df
record = {}
for col in thread_cols:
    if col == 'file_path':
        record[col] = file_path
    else:
        record[col] = mail.get(col)
thread_df = thread_df.append(record, ignore_index=True)

# %%
mail_df.head()
# %%
