#%%
import pandas as pd
import pprint
import json
#
from db import connect
engine = connect()
mail_df = pd.read_sql(sql='SELECT * FROM mail_54_original ORDER BY docno ASC',con=engine, index_col=None)
#
mail_df_json = mail_df.to_json(orient='index')
mail_df_json = json.loads(mail_df_json)
#
output = []
for document in mail_df_json.values():
    output.append(document)
#
path = '/Users/taroaso/myprojects/OpenIE/trec/2005/json/mails54.json'

with open(path, mode='w') as f:
    f.write(str(output))
#

# %%
