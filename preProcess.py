from nltk import tokenize
import re

def cleaningText(message):
    cleaned_message = re.sub(r'(=\n)','',message)
    cleaned_message = re.sub(r'(\[IMAGE\])','',cleaned_message)
    cleaned_message = re.sub(r'(=09)','',cleaned_message)
    return cleaned_message

def toSentences(message):
    cleaned_message = cleaningText(message)
    sentences = tokenize.sent_tokenize(cleaned_message)
    for i,s in enumerate(sentences):
        sentences[i] = re.sub(r'\n{1,}',' ',s)
        sentences[i] = re.sub(r'\s{2,}','',sentences[i])
    return sentences