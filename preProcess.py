#%%
from nltk import tokenize
import re

#%%
def cleaningText(message):
    cleaned_lines = []
    original_lines = message.splitlines()
    check1 = re.compile(r'^(\W{2,}.+)') #記号が2連続以上続く
    check2 = re.compile(r'^(_{2,}.+)') #_が2連続以上続く
    check3 = re.compile(r'^(On \w{3}, \w{3} [0-9]{1,2}, [0-9]{4} at [0-9]{1,2}:[0-9]{1,2} (A|P)M .+)') #先行メールを示す
    for line in original_lines:
        if line == '':
            continue
        # 行のトークン数が4未満なら
        elif len(line.split()) < 4:
            continue
        elif check1.match(line) is True:
            continue
        elif check2.match(line) is True:
            continue
        # 先行メールの本文を示すセンテンスが出現したら，それ以降の文章は確認しない（センテンスに含めない）
        elif check3.match(line) is True:
            break
        else:
            cleaned_lines.append(line)
            
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