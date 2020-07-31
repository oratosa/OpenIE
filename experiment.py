# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import os, sys, email, re, time
import numpy as np
import pandas as pd
from nltk import tokenize

# %%
#ドキュメント（メッセージ）をセンテンスに分解する
from preProcess import toSentences

def sentenceDataFrame(df):
    sent_dict = {'Message-ID':[],
                'Sentence-ID':[],
                'Sentence':[]}

    for i,message in enumerate(df['Message']):
        sentences = toSentences(message)
        sent_dict['Message-ID'].extend([df['Message-ID'][i]] * len(sentences))
        sent_dict['Sentence-ID'].extend(range(len(sentences)))
        sent_dict['Sentence'].extend(sentences)

    sentence_df = pd.DataFrame.from_dict(sent_dict,orient='columns')
    
    return sentence_df

# %%
# センテンスからトリプルを抽出する
from extraction import tripleExtraction, entityExtraction, NERtripleExtraction

def tripleDataFrame(sentence_df):
    triple_dict = {'Message-ID':[],
                 'Sentence-ID':[],
                 'Triple':[]}

    for i, sentence in enumerate(sentence_df['Sentence']):
        triples = tripleExtraction(sentence)
        entities = entityExtraction(sentence)
        nertriples = NERtripleExtraction(triples, entities)
        if nertriples is None:
            pass
        else:
            triple_dict['Message-ID'].extend([sentence_df['Message-ID'][i]] * len(nertriples))
            triple_dict['Sentence-ID'].extend([sentence_df['Sentence-ID'][i]] * len(nertriples))
            triple_dict['Triple'].extend(nertriples)

    triple_df = pd.DataFrame.from_dict(triple_dict,orient='columns')

    return triple_df

# %%
from loadFile import getDirList, getFileList, fileToDataFrame

# ディレクトリ 内のメールファイルを読み込む
directory_path = input() #"enron/maildir/allen-p/"
dir_list = getDirList(directory_path)

for directory in dir_list:
    if directory == directory_path:
        pass
    else:
        total_start = time.time()
        print('Processing on {}'.format(directory))
        file_list = getFileList(directory)
        # メールのテキストファイルをデータフレームに格納する
        start = time.time()
        df = fileToDataFrame(file_list)
        end = time.time()
        print('-- {}s for storing {} text files to a dataframe'.format(end-start, len(df)))
        # メッセージ本文をセンテンスに分解する
        start = time.time()
        sentence_df = sentenceDataFrame(df)
        end = time.time()
        print('-- {}s for decomposition to {} sentences'.format(end-start, len(sentence_df)))
        # センテンスからトリプルを抽出する
        start = time.time()
        triple_df = tripleDataFrame(sentence_df)
        end = time.time()
        print('-- {}s for extraction of {} triples'.format(end-start, len(triple_df)))
        # 各データフレームを結合して出力する
        start = time.time()
        output = pd.merge(df[['Path','Message-ID','Subject']],pd.merge(sentence_df,triple_df,on=['Message-ID','Sentence-ID']),on='Message-ID')
        output = output[['Path','Subject','Sentence-ID','Sentence','Triple']]
        directory = directory.replace('/','_')
        output.to_csv('output/{}.csv'.format(directory))
        end = time.time()
        print('-- {}s on output'.format(end-start))
        print('-- Total time: {}s'.format(end-total_start))

# %%
