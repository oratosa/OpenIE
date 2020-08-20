#%%
from nltk import tokenize
import re

#%%
def cleaningText(message):
    cleaned_lines = []
    original_lines = message.splitlines()
    for line in original_lines:
        if line == '':
            continue
        # 先行メールの本文を示すセンテンスが出現したら，それ以降の文章は除去する
        elif re.match(r'^(On \w{3}, \w{3} [0-9]{1,2}, [0-9]{4} at [0-9]{1,2}:[0-9]{1,2} (A|P)M .+)',line) is None:
            cleaned_lines.append(line)
        else:
            break
            
    # 行ごとに分割されているので， 1つの文章に戻し， sentence_tokenizerに入力できるようにする.
    cleaned_message = ' '.join(map(str, cleaned_lines))
    return cleaned_message

#%%
def toSentences(message):
    cleaned_message = cleaningText(message)
    sentences = tokenize.sent_tokenize(cleaned_message)

    #  改行コードがあれば空白に，空白文字が2つ以上続けば空白に，置換する
    for i,s in enumerate(sentences):
        sentences[i] = re.sub(r'\n{1,}',' ',s)
        sentences[i] = re.sub(r'\s{2,}',' ',sentences[i])
    return sentences